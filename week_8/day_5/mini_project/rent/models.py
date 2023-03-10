from django.db import models

# Create your models here.


# Customer model
class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=80)
    city = models.CharField(max_length=30)
    country = models.CharField(max_length=70)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


# Vehicle type
class VehicleType(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


# Vehicle size
class VehicleSize(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


# Vehicle
class Vehicle(models.Model):
    vehicle_type = models.ForeignKey(VehicleType, on_delete=models.CASCADE)
    vehicle_size = models.ForeignKey(VehicleSize, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    real_cost = models.FloatField()

    def __str__(self):
        return f"{self.vehicle_type} {self.vehicle_size}"


# Rental
class Rental(models.Model):
    rental_date = models.DateTimeField(auto_now_add=True)
    return_date = models.DateTimeField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)


# Rental Rate
class RentalRate(models.Model):
    daily_rate = models.FloatField()
    vehicle_type = models.ForeignKey(VehicleType, on_delete=models.CASCADE)
    vehicle_size = models.ForeignKey(VehicleSize, on_delete=models.CASCADE)
