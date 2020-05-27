from django.shortcuts import render

# Create your views here.
def home(request):
    numbers={1,2,3,4,5}
    eMail='rgkogan@gmail.com'
    args={'myEMail': eMail,'numbers':numbers}
    return render(request, 'accounts/home.html',args)