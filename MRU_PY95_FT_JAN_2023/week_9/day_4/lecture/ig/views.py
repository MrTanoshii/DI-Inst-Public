from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt

from .forms import PostFormSet
from .models import Post, Category

# Create your views here.


def posts(request, id):
    context = {
        "page_title": "Posts",
    }

    user = User.objects.get(pk=id)

    if request.POST:
        formset = PostFormSet(request.POST, queryset=Post.objects.filter(author=user))

        if formset.is_valid():
            print("--FORM VALID--")
            for form in formset:
                instances = form.save(commit=False)
                categories = form.cleaned_data["categories"]
                # get the categories from the form
                instances.categories.set(categories)
                # mofidy the categories of the instance accordingly
                instances.save()
            return render(request, "create_post.html", context)
        else:
            print("---ERRORS---", form.errors)
            context["formset"] = PostFormSet(queryset=Post.objects.filter(author=user))
            return render(request, "create_post.html", context)
    else:
        # GET, generate blank form
        context["formset"] = PostFormSet(queryset=Post.objects.filter(author=user))
    return render(request, "create_post.html", context)


@csrf_exempt
def test(request):
    context = {
        "page_title": "Test",
    }
    return render(request, "test.html", context)
