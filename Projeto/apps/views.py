from django.shortcuts import render, redirect
from . models import *
from django.http import HttpResponse

def login(request):
    return render(request, "apps/login.html")

