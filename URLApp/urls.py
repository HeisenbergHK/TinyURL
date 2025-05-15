from django.urls import path

from . import views

app_name = "URLApp"

urlpatterns = [
    path("", views.create_short_url, name="create"),
    path("<str:short_code>/", views.redirect_to_original, name="redirect"),
]
