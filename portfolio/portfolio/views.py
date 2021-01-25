from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request,'index.html')

def about(request):
    return HttpResponse("This is our About Page")

def contact(request):
    return HttpResponse("This is our Contact Page")


