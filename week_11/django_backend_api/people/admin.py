from django.contrib import admin

from .models import Person, PhysicalAddress

# Register your models here.

admin.site.register(Person)
admin.site.register(PhysicalAddress)
