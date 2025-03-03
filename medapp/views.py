from django.shortcuts import render, redirect
from medapp.models import *

# Create your views here.
def home(request):
    return render(request, 'index.html')

def starter(request):
    return render(request, 'starter-page.html')

def about(request):
    return render(request, 'about.html')
def service(request):
    return render(request, 'services.html')
def department(request):
    return render(request, 'departments.html')

def doctor(request):
    return render(request, 'doctor.html')



def contact(request):
    if request.method == 'POST':
        mycontact = Contact(
            name=request.POST['name'],
            email=request.POST['email'],
            subject=request.POST['subject'],
            message=request.POST['message'],
        )
        mycontact.save()
        return redirect('/contact')
    else:
        return render(request, 'contact.html')


def appointment(request):
   if request.method == 'POST':
      myappointments = Appointment(
          name=request.POST['name'],
          email=request.POST['email'],
          phone=request.POST['phone'],
          date=request.POST['date'],
          department=request.POST['department'],
          doctor=request.POST['doctor'],
          message=request.POST['message']
      )
      myappointments.save()
      return redirect('/show')
   else:
       return render(request, 'appointment.html')

def show(request):
    all = Appointment.objects.all()
    return render(request, 'show.html',{'all':all})

def delete(request,id):
    deleteappointment = Appointment.objects.get(id=id)
    deleteappointment.delete()
    return redirect('/show')





