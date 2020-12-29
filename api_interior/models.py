from django.db import models
from phone_field import PhoneField


# Create your models here.

class interior(models.Model):
    name = models.CharField(max_length = 100)
    email = models.EmailField(max_length = 100)
    phoneno = PhoneField(blank=True, default = True)
    message = models.CharField(max_length = 300)

    def __str__(self):
        return self.name

class login(models.Model):
    username = models.CharField(max_length = 30)
    password = models.CharField(max_length = 30)