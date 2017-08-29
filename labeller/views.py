from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ImageUploadForm
from .models import Image


def image_upload(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('labeller:index')
    else:
        form = ImageUploadForm()
    return render(request, 'image_upload_form.html', {'form': form})


def list_view(request):
    imgs = Image.objects.all()
    if imgs.count() >= 20:
        imgs = imgs[:20]
    return render(request, 'list_view.html', {'images': imgs})


def index(request):
    return HttpResponse('''Index for labeller app.
<a href="upload">upload</a> <a href="list">list</a>''')
