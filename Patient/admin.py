from django.contrib import admin
from .models import Doctor_Appointment
from .models import PatientTestReport
# Register your models here.
admin.site.register(Doctor_Appointment)
admin.site.register(PatientTestReport)

