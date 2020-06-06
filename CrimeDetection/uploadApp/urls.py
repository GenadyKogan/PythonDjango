from django.contrib import admin
from django.conf.urls import url
from . import views


urlpatterns = [
  #url('', views.upload,name='upload'),
  url('', views.uploadImg,name='uploadImg'),
]

