from django.shortcuts import render, redirect
from .forms import ImageUploadForm
from django.http import HttpResponse
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
    ims = Image.objects.all()

    return render(request, 'list_view.html', {'images': ims})


def index(request):
    return HttpResponse('index does nothing. <a href="upload">upload</a> <a href="list">list</a>')

# Create your views here.
