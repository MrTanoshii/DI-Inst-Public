from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

from datetime import datetime

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    released_date = models.DateField(default=datetime.now())
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse("posts")

    def __str__(self):
        return f"{self.title}"


class Category(models.Model):
    name = models.CharField(max_length=50)
    posts = models.ManyToManyField(Post, related_name="categories", blank=True)
    # ManyToMany relationships

    def __str__(self):
        return f"Category {self.name}"
