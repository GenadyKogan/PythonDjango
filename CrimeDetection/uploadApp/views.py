from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.files.storage import FileSystemStorage
from django.core.files.base import ContentFile
from PIL import Image
from base64 import decodestring

import os

from django.conf import settings


# Create your views here.
def upload(request):
    context = {}
    if request.method=='POST':
        username = request.user.username
        print(username)
        imagestr = request.body
        image = ContentFile(imagestr)
        image_name = request.headers.get("filename")
        fs=FileSystemStorage("uploadApp/static/media/image/"+username)
        name=fs.save(image_name,image)
        url=fs.url(name)
        context['url']=fs.url(name)
    return render(request, 'upload.html',context)
    


def uploadImg(request):
    username = request.user.username
    image_list=[]
    
    for root, dirs, files in os.walk(settings.MEDIA_ROOT+username):
        for file in files:
            image_list.append(os.path.join(root, file))
    return render(request, 'displayImg.html',{'brands': image_list})




