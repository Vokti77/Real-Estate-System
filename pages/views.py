from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'pages/index.html')


def about(request):
    return render(request, 'pages/about.html')


def home(request):
    return HttpResponse("home")


def base(request):
    return render(request, 'base.html')