from django.forms import ModelForm
from .models import*

class DoctorForm(ModelForm):

    class Meta:
        model = Doctor
        fields = "__all__"

class PatientForm(ModelForm):
   
    class Meta:
        model = Patient
        
        
        fields = ['patientname','password','mobile','symptoms','doctorname','admitDate']



class AppointmentForm(ModelForm):

    class Meta:
        model = Appointment
        fields = ['patientname','doctorname','appointmentDate']               

    





