from django.urls import path  # path function
from . import views  # . is shorthand for the current directory

# one urlpattern per line
urlpatterns = [
    path("", views.index, name="index"),
    path("test", views.test),
    path("about_website", views.about),
]

# '' : empty string and /
# views.index : index function in views.py
# name='index' : name of the route
