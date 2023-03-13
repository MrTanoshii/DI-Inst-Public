from django import forms
from .models import Category, Person, Post  # import the Post model from polls/models.py


class ContactForm(forms.Form):
    name = forms.CharField(required=False)
    email = forms.EmailField()
    comment = forms.CharField()


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = "__all__"
        # fields = ["first_name", "last_name"]
        # exclude = ["birth_date"]


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = "__all__"
        # fields = ["title", "text", "author"]
        exclude = ["released_date"]

        widgets = {
            "text": forms.Textarea(attrs={"class": "textarea"}),
            "author": forms.Select(attrs={"class": "select"}),
        }


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__"

        widgets = {
            "posts": forms.SelectMultiple(attrs={"class": "select"}),
        }
