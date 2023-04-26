from django.contrib import admin
from .models import Patient, MedicalData, EmergencyContact#, FingerprintData



class MedicalDataInline(admin.StackedInline):
    model = MedicalData
    extra = 0

class EmergencyContactInline(admin.StackedInline):
    model = EmergencyContact
    extra = 0
'''
class FingerprintDataInline(admin.StackedInline):
    model = FingerprintData
    extra = 0'''


class PatientAdmin(admin.ModelAdmin):
    list_display= ('name','dob','age','gender','phone','email','address','last_updated_time','last_updated_by')
    inlines = [MedicalDataInline, EmergencyContactInline]#, FingerprintDataInline]

admin.site.register(Patient, PatientAdmin)
