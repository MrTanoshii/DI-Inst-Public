from django.urls import path
from . import views

urlpatterns = [
    path("test", views.test, name="test"),
    path("", views.PostFormSet, name="create_post"),
    path("create_post/<int:id>", views.posts, name="create_post"),
]
