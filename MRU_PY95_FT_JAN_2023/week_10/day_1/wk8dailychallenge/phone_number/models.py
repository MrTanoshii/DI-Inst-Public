from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.


class Person(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    phone_number = PhoneNumberField(region="MU")
    address = models.CharField(max_length=150)
