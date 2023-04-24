from django.urls import path  # path function
from . import views  # . is shorthand for the current directory

# one urlpattern per line
urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("email", views.email, name="email"),
]
