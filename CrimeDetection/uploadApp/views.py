from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.files.storage import FileSystemStorage
# Create your views here.
def upload(request):
    context={}
    if request.method=='POST':
        upload_file=request.FILES['document']
        fs=FileSystemStorage()
        name=fs.save(upload_file.name,upload_file)
        #print(upload_file.name)
        #print(upload_file.size)
        #url=fs.url(name)
        #print(url)
        context['url']=fs.url(name)
    return render(request, 'upload.html',context)
    