from django.shortcuts import render

from .models import Customer, VehicleSize, VehicleType, Vehicle

from faker import Faker
from faker_vehicle import VehicleProvider
import random

# Create your views here.


def fake_data(request):
    fake = Faker()
    fake.add_provider(VehicleProvider)

    # # Add customers
    for _ in range(5000):
        first_name = fake.first_name()
        last_name = fake.last_name()
        email = fake.email()
        phone_number = fake.msisdn()
        address = fake.address()
        city = fake.city()
        country = fake.country()

        Customer.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone_number=phone_number,
            address=address,
            city=city,
            country=country,
        )

        # print(
        #     f"{first_name} {last_name} {email} {phone_number} {address} {city} {country}"
        # )

    # customers = Customer.objects.all()

    # for customer in customers:
    #     print(customer)

    # Add vehicle types
    # for _ in range(5):
    #     vehicle_type = fake.vehicle_model()
    #     VehicleType.objects.create(name=vehicle_type)

    vehicle_types = VehicleType.objects.all()

    for vehicle_type in vehicle_types:
        print(vehicle_type)

    # Add vehicle sizes
    # VehicleSize.objects.create(name="Small")
    # VehicleSize.objects.create(name="Medium")
    # VehicleSize.objects.create(name="Large")

    vehicle_sizes = VehicleSize.objects.all()

    for vehicle_size in vehicle_sizes:
        print(vehicle_size)

    # Add vehicles
    for _ in range(10000):
        rand_vehicle_type = random.choice(vehicle_types)
        rand_vehicle_size = random.choice(vehicle_sizes)
        vehicle_datetime = fake.date_time()
        vehicle_real_cost = random.uniform(800000, 10000000)

        Vehicle.objects.create(
            vehicle_type=rand_vehicle_type,
            vehicle_size=rand_vehicle_size,
            date_created=vehicle_datetime,
            real_cost=vehicle_real_cost,
        )

    # vehicles = Vehicle.objects.all()

    # for vehicle in vehicles:
    #     print(vehicle)

    return render(request, "fake_data.html")
