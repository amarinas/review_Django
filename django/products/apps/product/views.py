from django.shortcuts import render, redirect

def index(request):
    return render(request, "product/index.html")

# Create your views here.
