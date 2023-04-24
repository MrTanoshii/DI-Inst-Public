from django.shortcuts import render  # this line is added automatically
from django.http import HttpResponse  # pass view information into the browser

import datetime


# takes a request, returns a response
def index(request):
    # return HttpResponse("Hello DEV INST MRU, how are you doing today?")
    # return HttpResponse("test.html")
    context = {}
    return render(request, "base.html", context)


def test(request):
    context = {
        "user": "Jeffrey",
        "user2": "Jasmine",
        "lucky_number": {"Jacob": 7, "Tushil": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]},
        "bunch_of_text": "Arcade can be installed like any other Python Package. Arcade needs support for OpenGL 3.3+. It does not run on Raspberry Pi or Wayland. If you are familiar with Python package management you can just “pip install” Arcade. For more detailed instructions see Installation Instructions.",
        "order_date": datetime.datetime.now(),
        "item_total": "$65449068540",
        "subjects": [
            {"title": "Maths", "author": "Martine"},
            {"title": "English", "author": "Soobhug"},
            {"title": "Biology", "author": "Cynthia"},
            {"title": "Chemistry", "author": "Yushi"},
        ],
        "gender": "M",
    }
    return render(request, "test.html", context)


def about(request):
    context = {}
    return render(request, "about.html", context)
