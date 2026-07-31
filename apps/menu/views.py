from django.shortcuts import render, redirect, get_object_or_404

from .models import Food, Category
from .forms import FoodForm


def menu_list(request):

    foods = Food.objects.all()

    category = request.GET.get("category")

    if category:
        foods = foods.filter(category__name=category)

    search = request.GET.get("search")

    if search:
        foods = foods.filter(name__icontains=search)

    return render(
        request,
        "menu/menu.html",
        {
            "foods": foods,
            "categories": Category.objects.all(),
        },
    )


def food_detail(request, pk):

    food = get_object_or_404(Food, pk=pk)

    return render(
        request,
        "menu/food_detail.html",
        {
            "food": food
        }
    )


def add_food(request):

    if request.method == "POST":

        form = FoodForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            form.save()

            return redirect("menu")

    else:

        form = FoodForm()

    return render(
        request,
        "menu/add_food.html",
        {
            "form": form
        }
    )
