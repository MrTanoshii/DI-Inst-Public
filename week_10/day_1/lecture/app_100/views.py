from django.shortcuts import render

# Create your views here.


def index(request):
    context = {}

    return render(request, "index_main.html", context)


def good_night(request):
    return render(request, "good_night.html")
