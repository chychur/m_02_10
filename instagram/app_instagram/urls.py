from django.urls import path
from . import views

app_name = "app_instagram"

urlpatterns = [
    path("", views.main, name="main"),
    path("upload/", views.upload, name="upload"),
    path("pictures/", views.pictures, name="pictures")
]
