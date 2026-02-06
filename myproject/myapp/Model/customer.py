from django.db import models
from django.contrib.auth.models import User


class CustomerProfile(models.Model):
    users = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50, blank=True, default="")
    last_name=models.CharField(max_length=50,blank=True, default="")
    phone = models.CharField(max_length=15)
    address = models.TextField()

    def __str__(self):
        return self.users.username
    