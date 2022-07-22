from django.db import models
from django.contrib.auth.models import User

class Doctor(models.Model):
    doctorname = models.CharField(max_length=25,unique = True)
    password = models.CharField(max_length=25)
    qualification = models.CharField(max_length=50)
    mobile = models.CharField(max_length=20,null=True)
    department= models.CharField(max_length=50)
    status=models.BooleanField(default=False)
    
    def __str__(self):
        return str(self.doctorname) 
    
class Patient(models.Model):
    patientname = models.CharField(max_length=25,unique = True)
    password = models.CharField(max_length=25)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20,null=False)
    symptoms = models.CharField(max_length=100,null=True)
    doctorname= models.ForeignKey(Doctor,on_delete=models.CASCADE)
    admitDate=models.DateField()
    status=models.BooleanField(default=False)

    def __str__(self):
        return str(self.patientname) 
    
class Appointment(models.Model):
    patientname=models.ForeignKey(Patient,on_delete=models.CASCADE)
    doctorname=models.ForeignKey(Doctor,on_delete=models.CASCADE)
    appointmentDate=models.DateField()
    status=models.BooleanField(default=False)
    