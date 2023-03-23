from django import forms
from phonenumber_field.formfields import PhoneNumberField

from .models import Person


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ["name"]
        # fields = ["name", "phone_number"] # This doesn't work
        # exclude = ["id", "email", "address"]
        # field name is not required

    def __init__(self, *args, **kwargs):
        super(PersonForm, self).__init__(*args, **kwargs)
        self.fields["name"].required = False

    phone_number = PhoneNumberField(region="MU", required=False)
