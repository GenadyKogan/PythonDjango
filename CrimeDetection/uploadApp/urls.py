from django.contrib import admin
from django.conf.urls import url
from . import views


urlpatterns = [
  
  url(r'^$', views.upload,name='upload'),
  url('display/', views.uploadImg,name='uploadImg'),
]

