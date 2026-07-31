from decimal import Decimal
import threading

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from apps.menu.models import Food
from .models import Order, OrderItem
from .forms import CheckoutForm
from .tasks import update_order_status


@login_required
def checkout(request):

    cart = request.session.get("cart", {})

    if not cart:
        messages.warning(request, "Your cart is empty!")
        return redirect("cart")


    total = Decimal("0.00")

    for item in cart.values():
        item["subtotal"] = Decimal(
            str(item["price"])
        ) * item["quantity"]

        total += item["subtotal"]


    if request.method == "POST":

        form = CheckoutForm(request.POST)

        if form.is_valid():

            order = form.save(commit=False)

            order.user = request.user
            order.total_amount = total
            order.status = "Pending"
            order.payment_method = "COD"
            order.payment_status = "Pending"

            order.save()


            # automatic status update
            threading.Thread(
                target=update_order_status,
                args=(order.id,),
                daemon=True
            ).start()


            for food_id, item in cart.items():

                food = Food.objects.get(
                    id=food_id
                )

                OrderItem.objects.create(
                    order=order,
                    food=food,
                    quantity=item["quantity"],
                    price=item["price"],
                )


            request.session["cart"] = {}

            messages.success(
                request,
                "Order placed successfully!"
            )

            return redirect(
                "order_success"
            )


    else:
        form = CheckoutForm()


    return render(
        request,
        "orders/checkout.html",
        {
            "form": form,
            "cart": cart,
            "total": total,
        }
    )



@login_required
def order_success(request):

    return render(
        request,
        "orders/order_success.html"
    )



@login_required
def order_history(request):

    orders = Order.objects.filter(
        user=request.user
    ).order_by("-ordered_at")


    steps = [
        "Pending",
        "Confirmed",
        "Preparing",
        "Delivery",
        "Delivered"
    ]


    return render(
        request,
        "orders/order_history.html",
        {
            "orders": orders,
            "steps": steps
        }
    )