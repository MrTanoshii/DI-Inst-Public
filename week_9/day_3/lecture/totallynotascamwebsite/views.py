from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import authenticate, login

from django.contrib.auth.models import User

# from .models import User
from .forms import UserRegisterForm


class UserRegister(generic.CreateView):
    template_name = "register.html"
    model = User
    form_class = UserRegisterForm
    success_url = "success3"
    failed_message = "The User couldn't be added"

    def form_valid(self, form):
        user_to_add = form.cleaned_data
        # check the data we get when the form is valid
        print("user_to_add", user_to_add)

        super(UserRegister, self).form_valid(form)
        # inherit from ModelFormMixin : form_valid(form)
        # Saves the form instance, sets the current object for the view,
        # and redirects to get_success_url().

        print("---------form valid")

        # The form is valid, automatically sign-in the user
        user = authenticate(
            self.request,
            username=form.cleaned_data["username"],
            password=form.cleaned_data["password1"],
        )

        if user == None:
            print("---------user none")
            # User not validated for some reason, return standard form_valid() response
            # Inherit from TemplateResponseMixin :
            # render_to_response(context, **response_kwargs)¶
            return self.render_to_response(
                self.get_context_data(form=form, failed_message=self.failed_message)
            )

        else:
            print("-----------user good")
            # Log the user in
            login(self.request, user)
            # Redirect to success url
            # return redirect(reverse(self.get_success_url()))
            return redirect(self.get_success_url())


def success(request):
    return render(request, "success.html")


# import PostFormSet
from .forms import PostFormSet
from .models import Post


def posts(request, id):
    context = {
        "page_title": "Posts",
    }

    # get the user depending on the id passed in the url
    user = User.objects.get(pk=id)
    # get the userprofile linked to the user
    # userprofile = UserProfile.objects.get(user=user)

    if request.POST:
        # We use queryset in order to retrieve the posts of a specific user
        formset = PostFormSet(request.POST, queryset=Post.objects.filter(author=user))

        if formset.is_valid():
            # we don't save the instances yet
            instances = formset.save(commit=False)
            for instance in instances:
                # We're gonna do some processing here
                # blahblah
                print(instance)
                instance.save()
            return render(request, "base.html", context)
        else:
            print("---ERRORS---", form.errors)
            context["formset"] = PostFormSet(queryset=Post.objects.filter(author=user))
            return render(request, "create_post.html", context)
    else:
        # GET, generate blank form
        context["formset"] = PostFormSet(queryset=Post.objects.filter(author=user))
        return render(request, "create_post.html", context)
