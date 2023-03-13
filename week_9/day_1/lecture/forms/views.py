from django.shortcuts import render
from django import forms
from django.views import generic
from .models import Person, Post
from .forms import PersonForm, PostForm, CategoryForm

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
    person = Person.objects.get(first_name="Alexis")

    context = {
        "user": person,
        "page_title": "Posts",
        "posts": Post.objects.filter(
            author__first_name=person.first_name, author__last_name=person.last_name
        ),
    }

    if request.method == "POST":
        # POST, generate bound form with data from the request
        form = PostForm(request.POST)
        # check if it's valid:
        if form.is_valid():
            post_to_add = form.save(commit=False)
            # will return an object that hasn’t yet been saved to the database
            for attr, value in post_to_add.__dict__.items():
                print(f"{attr} : {value}")

            return render(request, "posts/homepage.html", context)
        else:
            print("---ERRORS---", form.errors)
            context["form"] = form
            return render(request, "posts/homepage.html", context)

    else:
        # GET, generate blank form
        context["form"] = PostForm()
    return render(request, "posts/homepage.html", context)


def signup(request):
    context = {
        "page_title": "SignUp",
    }

    if request.method == "POST":
        # POST, generate bound form with data from the request
        form = PersonForm(request.POST)  # the Person Form
        # check if it's valid:
        if form.is_valid():
            # person_to_add = form.save(commit=False)
            person_to_add = form.save(commit=True)
            print(person_to_add)
            for attr, value in person_to_add.__dict__.items():
                print(f"{attr} : {value}")

            form_first_name = form.cleaned_data["first_name"]
            form_last_name = form.cleaned_data["last_name"]
            form_birth_date = form.cleaned_data["birth_date"]
            form_has_pet = form.cleaned_data["has_pet"]
            form_number_pet = form.cleaned_data["number_pet"]
            context["formInfo"] = {
                "first_name": form_first_name,
                "last_name": form_last_name,
                "birth_date": form_birth_date,
                "has_pet": form_has_pet,
                "number_pet": form_number_pet,
            }
            print(context["formInfo"])
            context["success_msg"] = "You have successfully signed up!"
            return render(request, "posts/signup.html", context)
        else:
            print("---ERRORS---", form.errors)
            context["form"] = form
            return render(request, "posts/signup.html", context)

    else:
        # GET, generate blank form
        context["form"] = PersonForm()
    return render(request, "posts/signup.html", context)


def category(request):
    context = {
        "page_title": "Category",
    }

    if request.method == "POST":
        # POST, generate bound form with data from the request
        form = CategoryForm(request.POST)  # the Person Form
        # check if it's valid:
        if form.is_valid():
            # person_to_add = form.save(commit=False)
            category_to_add = form.save(commit=True)
            print(category_to_add)
            for attr, value in category_to_add.__dict__.items():
                print(f"{attr} : {value}")

            form_name = form.cleaned_data["name"]
            form_posts = form.cleaned_data["posts"]
            context["formInfo"] = {
                "name": form_name,
                "posts": form_posts,
            }
            print(context["formInfo"])
            context["success_msg"] = "You have successfully added a category!"
            return render(request, "posts/category.html", context)
        else:
            print("---ERRORS---", form.errors)
            context["form"] = form
            return render(request, "posts/category.html", context)

    else:
        # GET, generate blank form
        context["form"] = CategoryForm()
    return render(request, "posts/category.html", context)


class PostIndex(generic.ListView):
    template_name = "posts/posts.html"
    model = Post
    context_object_name = "post_list"

    def get_context_data(self, **kwargs):
        # **kwargs contains keyword context initialization values (if any)
        # Call base implementation to get a context
        context = super(PostIndex, self).get_context_data(**kwargs)
        # Add context data to pass to template
        context["user"] = Person.objects.first()
        return context


class PersonCreateIndex(generic.CreateView):
    template_name = "posts/signup.html"
    form_class = PersonForm  # PostForm we created earlier in forms.py

    def form_valid(self, form):
        person_to_add = form.cleaned_data
        print(person_to_add)
        return super().form_valid(form)
        # if the form is valid, the post is added to the table


class PersonDeleteIndex(generic.DeleteView):
    template_name = "posts/delete.html"
    model = Person
    success_url = "/"
