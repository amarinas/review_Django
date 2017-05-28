from django.shortcuts import render, redirect
from .models import Schedule

# Create your views here.
def index(request):
    return render(request, 'appointment/index.html')

def create(request):
    print request.POST

    return redirect('/success')

def success(request):
    return render(request, 'appointment/success.html')
