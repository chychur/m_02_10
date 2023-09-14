from django.shortcuts import render, redirect
from .models import Picture
from .forms import PictureForm


# Create your views here.

def main(request):
    return render(request, "app_instagram/index.html", context={"title": "My Instagram"})


def upload(request):
    form = PictureForm(instance=Picture())
    if request.method == 'POST':
        form = PictureForm(
            request.POST,
            request.FILES,
            instance=Picture()
        )
        if form.is_valid():
            form.save()
            return redirect(to="app_instagram:main")
    return render(request, "app_instagram/upload.html", context={"title": "My Instagram", "form": form})


def pictures(request):
    pictures = Picture.objects.all()
    return render(request, "app_instagram/pictures.html", context={"title": "My Instagram", "pictures": pictures})

