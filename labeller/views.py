from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .forms import ImageUploadForm, ImageChoiceForm
from .models import Image, Choice, TotalVotes

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


def label_view(request, img_id=None):
    '''label_view:
with GET request, shows a random image;
user can label the image with a label from Choice model.

with POST request, processes data from form submit'''
    if request.method == 'GET':
        if img_id:
            img = Image.objects.get(pk=img_id)
        else:
            images = Image.objects.all()
            img = images[randint(0, images.count())]

        choices = Choice.objects.all()
        return render(request, 'label_view.html',
                      {'img': img, 'choices': choices,
                       'form': ImageChoiceForm()})
    else:  # 'POST'
        form = ImageChoiceForm(request.POST)
        if form.is_valid():
            selected_label = Choice.objects.get(pk=request.POST['choice'])
            vote_obj, created = TotalVotes.objects.get_or_create(
                image=Image.objects.get(pk=img_id),
                choice=selected_label
            )
            vote_obj.votes += 1
            vote_obj.save()
            return HttpResponseRedirect(reverse('labeller:label'))

        else:
            return HttpResponse("form is invalid (tried). <a href='/'>home</>")


def list_view(request):
    '''list_view shows up to 20 images'''
    imgs = Image.objects.all()
    if imgs.count() > 20:
        imgs = imgs[:20]

    return render(request, 'list_view.html', {'images': imgs})


def index(request):
    return HttpResponse('''Index does nothing.
<a href="upload">upload</a> <a href="list">list</a>''')
