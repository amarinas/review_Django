from django.shortcuts import render, HttpResponse
#Controller
# Create your views here.

def index(request):
    print("*" * 100)
    name = "Ali"
    return render(request, "first_app/index.html")

def show(request):
    return render(request, 'first_app/show_users.html')

def testimonials(request):
    return render(request, 'first_app/testimonials.html')

def projects(request):
    return render(request, 'first_app/project.html')

def about(request):
    return render(request, 'first_app/about.html')
