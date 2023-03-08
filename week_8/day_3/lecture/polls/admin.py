from django.contrib import admin
from .models import Person, Email, ImageProfile

# Register your models here.

admin.site.register(Person)
admin.site.register(Email)
admin.site.register(ImageProfile)
