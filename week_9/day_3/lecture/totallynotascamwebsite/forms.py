from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import modelformset_factory

from django.contrib.auth.models import User

from .models import Post


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    # we add the email field
    # we customize the form with new field (the fields need to be in the User model)
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "text"]
        exclude = ["author", "released_date"]
        widgets = {
            "text": forms.Textarea(attrs={"class": "textarea"}),
            "author": forms.Select(attrs={"class": "select"}),
        }


# the new formset
PostFormSet = modelformset_factory(Post, form=PostForm)
