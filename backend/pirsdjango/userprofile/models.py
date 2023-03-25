from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return self.user.username
