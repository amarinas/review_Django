from django.shortcuts import render, redirect, HttpResponse
from .models import Schedule

# Create your views here.
def index(request):


    return render(request, 'appointment/index.html')

def create(request):
    print request.POST
    if request.method == "GET":
        return redirect('/')
    appointment_check = Schedule.objects.make_appointment(request.POST['date'], request.POST['time'])
    if 'error' in appointment_check:
        error = make_appointment['error']
        for msg in error:
            messages.error(request, msg)
        return redirect('/')



    return redirect('/success')

def success(request):
    context={
    'appointments': Schedule.objects.all()
    }
    return render(request, 'appointment/success.html', context)
