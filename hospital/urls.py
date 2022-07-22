from django.contrib import admin
from django.urls import path
from .views import*

urlpatterns = [
    path('', home, name="home"),
    path('patient_login', patient_login, name="patient_login"),
    path('doctor_login', doctor_login, name="doctor_login"),
    path('patient_register', patient_register, name="patient_register"),
    path('view_appointment/<int:id>/', view_appointment, name="view_appointment"),
    path('add_appointment', add_appointment, name="add_appointment"),
    path('patient_logout', patient_logout, name="patient_logout"),
    
 
]