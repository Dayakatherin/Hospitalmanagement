from django.shortcuts import render,redirect
from .forms import AppointmentForm,PatientForm,DoctorForm
from .models import *
from django.http import HttpResponse
from django.contrib.auth import logout

def home(request):
    return render(request , 'index.html')

def patient_login(request):
    if request.method == 'POST':
        patientname = request.POST['patientname']
        password = request.POST['password']
        patient = Patient.objects.get(patientname=patientname,password=password)
        if patient:
            request.session['patient'] = patientname
            return redirect('add_appointment')
        else:
            return HttpResponse('Please enter valid Username or Password.') 
    else:
        return render(request,'patientloginform.html')

def doctor_login(request):
    if request.method == 'POST':
        doctorname = request.POST['doctorname']
        password = request.POST['password']
        doctor = Doctor.objects.get(doctorname=doctorname,password=password)
        if doctor:
            request.session['doctor'] = doctorname
            return redirect('view_appointment', id=doctor.id)
        else:
            return HttpResponse('Please enter valid Username or Password.') 
    else:
        return render(request,'doctorloginform.html')               


def patient_register(request):
    form = PatientForm()
    if request.method == "POST":
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
    if request.method == 'POST':
        patientname = request.POST['patientname']
        password = request.POST['password']
        patient = Patient.objects.get(patientname=patientname,password=password)
        if patient:
            request.session['patient'] = patientname
            return redirect('add_appointment')
            
    context = {'form':form}
    return render(request,'register.html',context)  
       

def add_appointment(request): 
    form = AppointmentForm()
    if request.method == "POST":
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_appointment')
    context = {'form':form}
    return render(request,'add_appointment.html',context)  
              
def view_appointment(request,id):
    appointments = Appointment.objects.filter(doctorname=id)
    print (appointments)
    return render(request, "appointment.html", {'appointments':appointments})      

def patient_logout(request):
    logout(request)
    return redirect('home')