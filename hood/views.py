from django.shortcuts import render
from .forms import SignupForm


def index(request):
    return render(request, 'index.html')


def signup(request):
    return render(request, 'registration/signup.html')
