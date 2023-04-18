from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path("name/", views.name, name="name"),
    path("phone_number/", views.phonenumber, name="phonenumber"),
    path("search", views.search, name="search"),
]
