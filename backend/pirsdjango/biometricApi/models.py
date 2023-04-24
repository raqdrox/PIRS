from django.db import models

# Create your models here.
class FingerprintIdMapping(models.Model):
    id=models.AutoField(primary_key=True)
    fingerprint = models.TextField(blank=True)

class PatientIdMapping(models.Model):
    finger_id=models.IntegerField(blank=True,default=-1)
    patient_id = models.IntegerField(blank=True,default=-1)



    
    