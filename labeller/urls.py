# labeller urls.py

from django.conf.urls import url
# from django.conf import settings

from . import views

app_name = 'labeller'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^upload/', views.image_upload, name='upload'),
    url(r'^list/', views.list_view, name='list')
]
