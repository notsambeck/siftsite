from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .forms import ImageUploadForm, ImageChoiceForm, TotalVotes
from .models import Image, Choice

from numpy.random import randint


def image_upload(request):
    '''image_upload is a view for uploading images.'''
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('labeller:index')
    else:
        form = ImageUploadForm()
    return render(request, 'image_upload_form.html', {'form': form})


def label_view(request):
    '''label_view is a view that shows a random image;
user can label the image with a label from Choice model'''
    images = Image.objects.all()
    img = images[randint(0, images.count())]
    choices = Choice.objects.all()
    if request.methiod == 'POST':
        form = ImageChoiceForm(request.POST)
        if form.is_valid():

            return HttpResponseRedirect(reverse('labeller:index'))
    else:
        return render(request, 'label_view.html', {'img': img,
                                                   'choices': choices})


def vote(request, image_id):
    selected_label = Choice.label.get(pk=request.POST['choice'])
    votesObj = TotalVotes.get(image=image_id, label=selected_label)
    votesObj.votes += 1
    votesObj.save()


def list_view(request):
    '''list_view shows up to 20 images'''
    imgs = Image.objects.all()
    if imgs.count() > 20:
        imgs = imgs[:20]

    return render(request, 'list_view.html', {'images': imgs})


def index(request):
    return HttpResponse('''Index does nothing.
<a href="upload">upload</a> <a href="list">list</a>''')
