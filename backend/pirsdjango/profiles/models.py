from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import AbstractUser


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    
    def __str__(self):
        return self.user.username
    

class User(AbstractUser):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE, null=True)