from django.urls import path
from . import views

urlpatterns = [
    path("register", views.UserRegister.as_view(), name="register"),
    path("success", views.success, name="success3"),
    path("create_post/<int:id>", views.posts, name="create_post"),
]
