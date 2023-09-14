import os

from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import PictureForm
from .models import Picture


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


def remove_picture(request, pic_id):
    pic = Picture.objects.filter(pk=pic_id, user=request.user) # , user=request.user
    try:
        os.unlink(os.path.join(settings.MEDIA_ROOT, str(pic.first().path)))
    except OSError as e:
        print(e)
    pic.delete()
    return redirect(to="app_instagram:pictures")


def edit_picture(request, pic_id):
    if request.method == "POST":
        description = request.POST["description"]
        Picture.objects.filter(pk=pic_id, user=request.user).update(description=description)
        return redirect(to="app_instagram:pictures")

    picture = Picture.objects.filter(pk=pic_id, user=request.user).first()
    ctx = {"title": "My Instagram", "picture": picture}
    return render(request, "app_instagram/edit.html", context=ctx)
