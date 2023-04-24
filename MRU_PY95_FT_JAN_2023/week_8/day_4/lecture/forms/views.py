from django.shortcuts import render
from django import forms
from .models import Person

# from .forms import ContactForm


class ContactForm(forms.Form):
    name = forms.CharField(
        required=False, widget=forms.TextInput(attrs={"class": "name_class"})
    )
    email = forms.EmailField(
        label="Type your email",
        help_text="Must contain al least 8 characters",
        error_messages={
            "required": "The email field is mandatory.",
            "invalid": "The email is invalid. Please provide a valid email.",
        },
    )
    comment = forms.CharField(widget=forms.Textarea)


# Create your views here.


def index(request):
    person = Person.objects.get(first_name="Ra'ees")

    context = {
        "page_title": "Homepage",
        "user": person,
        # "validity": f.is_valid(),
    }

    if request.method == "POST":
        # POST, generate form with data from the request
        form = ContactForm(request.POST)
        context["form"] = form

        print("data", form.data)

        # check if it's valid:
        if form.is_valid():
            form_name = form.cleaned_data["name"]
            form_email = form.cleaned_data["email"]
            form_comment = form.cleaned_data["comment"]
            context["formInfo"] = {
                "name": form_name,
                "email": form_email,
                "comment": form_comment,
            }
            # context['btnFormHidden'] = True # To hide the button is the form is successfully submitted
            # print the values to make sure their are correct
            print(context["formInfo"])
    else:
        context["form"] = ContactForm()

    return render(request, "posts/homepage.html", context)

    f = ContactForm({"name": "", "email": "mariagmail.com", "comment": "hello"})

    form_name = f["name"].value
    form_email = f["email"].value
    form_comment = f["comment"].value
    form_date = f["date"].value
    context["formInfo"] = [form_name, form_email, form_comment, form_date]

    return render(request, "posts/homepage.html", context)
