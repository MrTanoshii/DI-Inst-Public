from django.db import models
from django.urls import reverse
from datetime import datetime

# Create your models here.


class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    birth_date = models.DateField()
    has_pet = models.BooleanField(default=True)
    number_pet = models.IntegerField()

    def get_absolute_url(self):
        return reverse("posts")


class ImageProfile(models.Model):
    person = models.OneToOneField(
        Person,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    image = models.URLField()

    def __str__(self):
        return f"ImageProfile of {self.person}"


# p_a = Person(first_name="Alexis", last_name="Guilbert", number_pet=20)


class Post(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    released_date = models.DateField(default=datetime.now())
    author = models.ForeignKey(Person, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title}"


class Category(models.Model):
    name = models.CharField(max_length=50)
    posts = models.ManyToManyField(Post, related_name="categories", blank=True)
    # related_name is to retrieve the categories from a post

    def __str__(self):
        return f"Category {self.name}"


# Add a new model called Email that has a one to one relationship with the Person Model (a person has one email, and a email belongs to only one person). Do all the migrations and using the Django Shell, add an email adress to all the existing persons in the database.


class Email(models.Model):
    person = models.OneToOneField(
        Person,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    email = models.EmailField()

    def __str__(self):
        return f"Email of {self.person}"
