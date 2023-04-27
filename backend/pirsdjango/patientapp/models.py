import datetime
from django.db import models

class Patient(models.Model):
    id= models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    dob= models.DateField(default=datetime.date.today)
    gender = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email= models.CharField(max_length=100)
    address = models.CharField(max_length=1000)

    last_updated_time = models.DateTimeField(auto_now=True)
    last_updated_by = models.CharField(max_length=100,blank=True)
    
    @property
    def age(self):
        import datetime
        today = datetime.date.today()
        if self.dob:
            return str(today.year - self.dob.year - ((today.month, today.day) < (self.dob.month, self.dob.day)))
        else:
            return "0"
    def __str__(self):
        return self.name
    

class MedicalData(models.Model):
    patient = models.OneToOneField(Patient, on_delete=models.CASCADE,related_name='medical_data')
    blood_group = models.CharField(max_length=100,blank=True)
    diseases = models.CharField(max_length=1000,blank=True)
    allergies = models.CharField(max_length=1000,blank=True)

    height = models.IntegerField(default=0,blank=True)
    weight = models.IntegerField(default=0,blank=True)

    

    def __str__(self):
        return self.patient.name
    
class EmergencyContact(models.Model):
    patient = models.OneToOneField(Patient, on_delete=models.CASCADE,related_name='emergency_contact')
    name = models.CharField(max_length=100,blank=True)
    phone = models.CharField(max_length=100,blank=True)

    def __str__(self):
        return self.name
'''
class FingerprintData(models.Model):
    patient = models.OneToOneField(Patient, on_delete=models.CASCADE,related_name='fingerprint_data')
    fingerprint_data = models.TextField(blank=True)
    def __str__(self):
        return self.patient.name
        
'''