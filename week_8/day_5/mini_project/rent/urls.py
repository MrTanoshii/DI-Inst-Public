from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
    path("fake_data", views.fake_data),
]
