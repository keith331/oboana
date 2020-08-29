from django.http import HttpResponse
from django.shortcuts import render


# def homepage(request):
#     return HttpResponse('OBO Ananlyser')

def homepage(request):
    return render(request, 'home.html')

def goods(request):
    return HttpResponse('goods page')

def about(request):
    return render(request, 'about.html')
