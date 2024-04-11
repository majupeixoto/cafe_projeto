from django.shortcuts import render, redirect
from . models import *
from django.http import HttpResponse

def home(request):
    return render(request, "apps/home.html")