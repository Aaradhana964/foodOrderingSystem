from django import forms
from .models import Food, Category


class CategoryForm(forms.ModelForm):

    class Meta:

        model = Category

        fields = "__all__"


class FoodForm(forms.ModelForm):

    class Meta:

        model = Food

        fields = "__all__"

        widgets = {
            "description": forms.Textarea(attrs={"rows":4})
        }