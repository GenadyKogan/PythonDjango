from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.files.storage import FileSystemStorage
from django.core.files.base import ContentFile
from PIL import Image
from base64 import decodestring
import json

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
    