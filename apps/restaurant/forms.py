from django import forms
from .models import Restaurant


class RestaurantForm(forms.ModelForm):

    class Meta:

        model = Restaurant

        fields = "__all__"

        widgets = {

            "description": forms.Textarea(
                attrs={"rows": 5}
            )

        }