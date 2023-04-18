from django.shortcuts import render
from django.views.generic import FormView

from .forms import ContactForm

# Create your views here.


# def index(request):
#     return render(request, "index.html")


class DefaultFormView(FormView):
    template_name = "index.html"
    form_class = ContactForm
