from django.shortcuts import render
from .forms import RecommendationForm
from apps.menu.models import Food
from django.contrib.auth.decorators import login_required


@login_required
def recommend(request):

    foods = None

    if request.method == "POST":

        form = RecommendationForm(request.POST)

        if form.is_valid():

            goal = form.cleaned_data["goal"]

            budget = form.cleaned_data["budget"]

            cuisine = form.cleaned_data["cuisine"]

            foods = Food.objects.filter(
                price__lte=budget,
                restaurant__cuisine__icontains=cuisine
            )

    else:

        form = RecommendationForm()

    return render(
        request,
        "recommendation/recommend.html",
        {
            "form": form,
            "foods": foods
        }
    )