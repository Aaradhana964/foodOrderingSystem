from django import forms


class RecommendationForm(forms.Form):

    GOALS = [
        ("Weight Loss", "Weight Loss"),
        ("Weight Gain", "Weight Gain"),
        ("Maintain Weight", "Maintain Weight"),
    ]

    goal = forms.ChoiceField(choices=GOALS)

    budget = forms.DecimalField()

    cuisine = forms.CharField(max_length=100)