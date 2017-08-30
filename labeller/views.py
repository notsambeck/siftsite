from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .forms import ImageUploadForm, ImageChoiceForm
from .models import Image, Choice, TotalVotes
from .serializers import ImageSerializer

from numpy.random import randint

from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response


def image_upload(request):
    '''image_upload is a view for uploading images.'''
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('labeller:list')
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
            if images.count() > 0:
                img = images[randint(0, images.count())]
            else:
                return HttpResponse("no images uploaded. <a href='/'>home</>")

        choices = Choice.objects.all()
        if not choices.count():
            return HttpResponse("no choices created. <a href='/'>home</>")

        return render(request, 'label_view.html',
                      {'image': img, 'choices': choices,
                       'form': ImageChoiceForm()})
    elif request.method == 'POST':  # 'POST'
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
            return HttpResponse("form is invalid. <a href='/'>home</>")
    else:
        return HttpResponse("not a POST or GET request. <a href='/'>home</>")


def list_view(request):
    '''list_view shows up to 60 images'''
    imgs = Image.objects.all()
    last60 = imgs.count() - 60
    if last60 > 0:
        imgs = imgs[last60:]

    return render(request, 'list_view.html', {'images': imgs})


def results(request, img_id):
    '''show vote results for an image (by id)'''
    image = Image.objects.get(pk=img_id)
    choices = Choice.objects.all()
    votes = TotalVotes.objects.filter(image=image)
    return render(request, 'results_view.html',
                  {'image': image, 'votes': votes, 'choices': choices})


@api_view(['GET', 'POST'])
def api_image_list(request):
    '''
    List all images or create a new one
    '''
    if request.method == 'GET':
        images = Image.objects.all()
        serializer = ImageSerializer(images, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ImageSerializer(data=request.data)
        if serializer.is_valid():
            form = ImageUploadForm(serializer.data, request.FILES)
            if form.is_valid():
                form.save()
                return Response(serializer.data,
                                status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def api_image(request, img_id):
    '''
    List one image by id
    '''
    image = get_object_or_404(Image, pk=img_id)

    serializer = ImageSerializer(image)
    return Response(serializer.data)
