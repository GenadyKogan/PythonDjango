from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.files.storage import FileSystemStorage
from django.core.files.base import ContentFile
from PIL import Image
from base64 import decodestring
import json
import os

from django.conf import settings
from flask import Flask, request, render_template, send_from_directory

# Create your views here.
def upload(request):
    context = {}
    if request.method=='POST':
        imagestr = request.body
        image = ContentFile(imagestr)
        image_name = request.headers.get("filename")
        fs=FileSystemStorage()
        name=fs.save(image_name,image)
        url=fs.url(name)
        context['url']=fs.url(name)
    return render(request, 'upload.html',context)
    


def uploadImg(request):
    
    image_list=[]
    
    for root, dirs, files in os.walk(settings.MEDIA_ROOT):
        for file in files:
            image_list.append(file)
    return render(request, 'complete.html',{'brands': image_list})







def send_image(filename):
    return send_from_directory('mainApp/image/',filename)




def show_images(request):

    image_list=[]
    #app_static_dir = os.path.join(os.path.join(os.path.join(os.path.join(settings.BASE_DIR,'appname'),'static'),'images'),'brands')  #appname is your appname and brands is the folder that you mentioned
    app_static_dir='uploadApp/static/media/image/'
    
    for root, dirs, files in os.walk(settings.STATIC_ROOT):
        for file in files:
            if file.endswith(".jpg"):
                image_list.append(file)
    # TODO: Read list of existing Int Files and send data to feed the table
    return render(request, 'templates/complete.html', {'brands': image_list})



