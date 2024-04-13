from django.shortcuts import render, redirect
from . models import *

def login(request):
    return render(request, "apps/login.html")

