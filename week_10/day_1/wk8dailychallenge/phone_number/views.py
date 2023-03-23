from django.shortcuts import render, redirect
from .forms import PersonForm

from .models import Person

# Create your views here.


def name(request):
    if request.method == "GET":
        name = request.GET.get("name")

        # If name is not defined in the url, redirect to search
        if not name:
            return redirect("search")

        persons = Person.objects.all()
        print(persons)

        target_person = Person.objects.filter(name=name).first()
        # If the target person is not found in the database, redirect to search
        if not target_person:
            return redirect("search")

        print(target_person)
        context = {"name": name, "target_person": target_person}

        return render(request, "name.html", context)

    # If the method is not GET, redirect to search
    else:
        return redirect("search")

    # return render(request, "name.html")


def phonenumber(request):
    if request.method == "GET":
        phone_number = request.GET.get("phone_number")

        # If name is not defined in the url, redirect to search
        if not phone_number:
            return redirect("search")

        target_person = Person.objects.filter(phone_number=phone_number).first()
        # If the target person is not found in the database, redirect to search
        print(target_person)
        if not target_person:
            return redirect("search")

        context = {"name": target_person.name, "target_person": target_person}

    return render(request, "phonenumber.html", context)


def search(request):
    context = {"title": "Search", "form": PersonForm()}

    if request.method == "POST":
        form = PersonForm(request.POST)
        if form.is_valid():
            context["form"] = form
            context["name"] = form.cleaned_data["name"]
            context["phone_number"] = form.cleaned_data["phone_number"]

            print(context["name"])
            if context["name"]:
                return redirect("name", name=context["name"])

    return render(request, "search.html", context)
