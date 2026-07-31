from django.shortcuts import render, redirect, get_object_or_404
from apps.menu.models import Food
from apps.orders.models import Order
from .models import Restaurant
from .forms import RestaurantForm
from decimal import Decimal
from django.db.models import Sum
from django.contrib.auth.decorators import login_required


def restaurant_list(request):

    restaurants = Restaurant.objects.all()

    return render(
        request,
        "restaurant/restaurant_list.html",
        {
            "restaurants": restaurants
        }
    )


def restaurant_detail(request, pk):

    restaurant = get_object_or_404(
        Restaurant,
        pk=pk
    )

    return render(
        request,
        "restaurant/restaurant_detail.html",
        {
            "restaurant": restaurant
        }
    )


def add_restaurant(request):

    if request.method == "POST":

        form = RestaurantForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            form.save()

            return redirect("restaurant_list")

    else:

        form = RestaurantForm()

    return render(
        request,
        "restaurant/add_restaurant.html",
        {
            "form": form
        }
    )

@login_required
def dashboard(request):

    restaurant_count = Restaurant.objects.count()

    food_count = Food.objects.count()

    order_count = Order.objects.count()

    revenue = Order.objects.aggregate(
        total=Sum("total_amount")
    )["total"] or Decimal("0.00")


    return render(
        request,
        "restaurant/dashboard.html",
        {
            "restaurant_count": restaurant_count,
            "food_count": food_count,
            "order_count": order_count,
            "revenue": revenue,
        }
    )
