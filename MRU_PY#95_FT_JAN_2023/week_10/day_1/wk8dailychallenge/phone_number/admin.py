from django.contrib import admin
from django import forms
from .models import Person
from phonenumber_field.modelfields import PhoneNumberField
from phonenumber_field.widgets import (
    PhoneNumberInternationalFallbackWidget,
    RegionalPhoneNumberWidget,
)

# Register your models here.


class PersonAdmin(admin.ModelAdmin):
    formfield_overrides = {
        PhoneNumberField: {"widget": RegionalPhoneNumberWidget(region="MU")},
    }


admin.site.register(Person, PersonAdmin)

# admin.site.register(Person)
