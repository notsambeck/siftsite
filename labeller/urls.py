# labeller urls.py

from django.conf.urls import url
# from django.conf import settings

from . import views

app_name = 'labeller'
urlpatterns = [
    url(r'^$|index|list', views.list_view, name='list'),
    url(r'^upload/$', views.image_upload, name='upload'),
    url(r'^label/(?P<img_id>[0-9]*)$', views.label_view, name='label'),
    url(r'^label/$', views.label_view, name='label'),
    url(r'^results/(?P<img_id>[0-9]+)$', views.results, name='results'),
    url(r'^api/$', views.api_image_list),
    url(r'^api/(?P<img_id>[0-9]+)$', views.api_image),
    url(r'^x/$', views.ListImages.as_view()),
]
