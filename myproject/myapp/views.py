from django.shortcuts import render,HttpResponse

# Create your views here.

def base(request):
    return render(request,'base.html')

def home(request):
    return render(request,'home.html')

def contact(request):
    return render(request,'contact.html')

def login(request):
    return render(request,'login.html')


def ownership(request):
    return render(request,'ownership.html')
def service(request):
    return render(request,'service.html')