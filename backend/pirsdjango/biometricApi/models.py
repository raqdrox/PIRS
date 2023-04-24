from django.db import models

# Create your models here.
class FingerprintIdMapping(models.Model):
    id=models.AutoField(primary_key=True)
    fingerprint = models.TextField(blank=True)




    
    