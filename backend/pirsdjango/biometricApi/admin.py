from django.contrib import admin

# Register your models here.
from .models import PatientIdMapping

class PatientIdMappingAdmin(admin.ModelAdmin):
    list_display= ('finger_id','patient_id')

admin.site.register(PatientIdMapping, PatientIdMappingAdmin)