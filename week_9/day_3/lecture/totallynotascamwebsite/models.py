from django.db import models
from datetime import datetime

from django.contrib.auth.models import User

# Create your models here.


# class User(models.Model):
#     username = models.CharField(max_length=100)
#     email = models.EmailField()
#     password = models.CharField(max_length=100)


#     def __str__(self):
#         return self.username


# class Person(models.Model):
#     first_name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length=40)
#     birth_date = models.DateField()
#     has_pet = models.BooleanField(default=True)
#     number_pet = models.IntegerField()


class Post(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    released_date = models.DateField(default=datetime.now())
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title}"
