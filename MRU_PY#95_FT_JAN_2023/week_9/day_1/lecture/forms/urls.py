from django.urls import path  # path function
from . import views  # . is shorthand for the current directory

# one urlpattern per line
urlpatterns = [
    path("", views.index, name="index"),
    path("signup", views.PersonCreateIndex.as_view(), name="signup"),
    path("cat", views.category, name="category"),
    path("list_posts", views.PostIndex.as_view(), name="posts"),
    path("person/<int:pk>/delete", views.PersonDeleteIndex.as_view(), name="delete_person")
]
