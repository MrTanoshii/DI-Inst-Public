from django.core import serializers
from django.shortcuts import render, HttpResponse, HttpResponsePermanentRedirect

from .models import Person, PhysicalAddress

from faker import Faker

# Create your views here.


def all_people(request):
    people = Person.objects.all()
    people_json = serializers.serialize("json", people)

    return HttpResponse(people_json, content_type="application/json")


def person_detail(request, person_id):
    person = Person.objects.get(id=person_id)
    person_json = serializers.serialize("json", [person])

    return HttpResponse(person_json, content_type="application/json")


def person_by_first_name(request, first_name):
    people = Person.objects.filter(first_name=first_name)
    people_json = serializers.serialize("json", people)

    return HttpResponse(people_json, content_type="application/json")


def fake(request):
    fake = Faker()

    for _ in range(10):
        fake_person = Person(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            birth_date=fake.date_of_birth(),
        )
        fake_person.save()

        fake_address = PhysicalAddress(
            street=fake.street_address(),
            city=fake.city(),
            state=fake.state(),
            zip_code=fake.zipcode(),
            person=fake_person,
        )
        fake_address.save()

    return HttpResponsePermanentRedirect("/api/people/")
