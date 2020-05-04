from django.shortcuts import render

def index(request):
    return render(request, 'mainApp/homePage.html')
def contact(request):
    return render(request, 'mainApp/basic.html', {'values': ['If you have any questions:', 'rgkogan@gmail.com']})


