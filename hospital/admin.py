from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Doctor, Patient, Appointment


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'specialization', 'phone', 'email')
    search_fields = ('name', 'specialization', 'email')


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'date_of_birth', 'phone')
    search_fields = ('name', 'phone')


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'patient', 'doctor', 'appointment_date', 'reason'
    )
    search_fields = ('patient__name', 'doctor__name', 'reason')
    list_filter = ('appointment_date',)
