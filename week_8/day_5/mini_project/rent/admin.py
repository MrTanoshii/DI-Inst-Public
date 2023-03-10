from django.contrib import admin
from .models import Customer, VehicleSize, VehicleType, Vehicle

# Register your models here.
admin.site.register(Customer)
admin.site.register(VehicleSize)
admin.site.register(VehicleType)
admin.site.register(Vehicle)