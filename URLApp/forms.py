from django import forms

from .models import URL


class URLForm(forms.ModelForm):
    class Meta:
        model = URL
        fields = ["original_url"]
        widgets = {
            "original_url": forms.URLInput(
                attrs={"placeholder": "https://example.com", "class": "form-control"}
            )
        }
