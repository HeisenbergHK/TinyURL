from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views.decorators.http import require_http_methods

from .forms import URLForm
from .models import URL


@require_http_methods(["GET", "POST"])
def create_short_url(request):
    if request.method == "POST":
        form = URLForm(request.POST)
        if form.is_valid():
            original_url = form.cleaned_data["original_url"]
            # 🔍 Check for duplicates
            url = URL.objects.filter(original_url=original_url).first()
            if url is None:
                url = form.save(commit=False)
                if request.user.is_authenticated:
                    url.created_by = request.user
                url.short_code = (
                    url.generate_short_code()
                )  # make sure you have this method in your model
                url.save()

            short_url = request.build_absolute_uri(
                reverse("URLApp:redirect", args=[url.short_code])
            )
            return render(
                request,
                "URLApp/result.html",
                {"short_url": short_url, "original_url": url.original_url},
            )
    else:
        form = URLForm()

    return render(request, "URLApp/create.html", {"form": form})


def redirect_to_original(request, short_code):
    url = get_object_or_404(URL, short_code=short_code)
    url.click_count += 1
    url.save()
    return redirect(url.original_url)
