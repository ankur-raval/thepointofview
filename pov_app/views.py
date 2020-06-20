from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import get_user_model
User=get_user_model()
from . models import *


def index_view(request):
    return render(request, 'index.html')