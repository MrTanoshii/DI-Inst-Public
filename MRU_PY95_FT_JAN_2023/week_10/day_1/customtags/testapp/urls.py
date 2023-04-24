from django.urls import path
from django.views.generic.base import TemplateView

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("test", TemplateView.as_view(template_name="index.html"), name="test"),
]
