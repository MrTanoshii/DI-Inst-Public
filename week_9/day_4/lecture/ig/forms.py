from django import forms
from django.forms import modelformset_factory

from .models import Post, Category


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "text"]
        exclude = ["author", "released_date"]
        widgets = {
            "text": forms.Textarea(attrs={"class": "textarea"}),
        }

    def __init__(self, *args, **kwargs):  # we override the __init__ method
        super().__init__(*args, **kwargs)
        # What are the current categories?
        current_categories = self.instance.categories.all()

        # What are the all the possible categories?
        possible_categories = Category.objects.all()

        self.fields["categories"] = forms.ModelMultipleChoiceField(
            widget=forms.CheckboxSelectMultiple,
            queryset=possible_categories,
            initial=current_categories,
            required=False,
        )  # If it can be empty


# the new formset
PostFormSet = modelformset_factory(Post, form=PostForm, extra=0)
