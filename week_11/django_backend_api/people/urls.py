from django.urls import path

from . import views

urlpatterns = [
    path("people/", views.all_people, name="all_people"),
    path("people/id/<int:person_id>/", views.person_detail, name="person_detail"),
    path(
        "people/first_name/<str:first_name>/",
        views.person_by_first_name,
        name="person_by_first_name",
    ),
    path("fake", views.fake, name="fake"),
]
