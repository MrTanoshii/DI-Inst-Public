from django.shortcuts import render
from .models import Person

# Create your views here.


def homepage(request):
    context = {"user": Person.objects.get(first_name="Alexis")}
    return render(request, "homepage.html", context)


def email(request):
    context = {"user": Person.objects.get(first_name="Alexis")}
    return render(request, "email.html", context)
