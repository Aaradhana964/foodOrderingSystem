from django.shortcuts import redirect, render, get_object_or_404
from apps.menu.models import Food


def add_to_cart(request, food_id):

    food = get_object_or_404(Food, id=food_id)

    cart = request.session.get("cart", {})

    food_id = str(food.id)

    if food_id in cart:
        cart[food_id]["quantity"] += 1
    else:
        cart[food_id] = {
            "name": food.name,
            "price": float(food.price),
            "image": food.image.url,
            "quantity": 1,
        }

    request.session["cart"] = cart

    return redirect("cart")
def cart(request):
    cart = request.session.get("cart", {})
    total = 0

    for item in cart.values():
        subtotal = item["price"] * item["quantity"]
        item["subtotal"] = subtotal
        total += subtotal

    return render(
        request,
        "cart/cart.html",
        {
            "cart": cart,
            "total": total,
        },
    )
def remove_item(request, food_id):

    cart = request.session.get("cart", {})

    food_id = str(food_id)

    if food_id in cart:
        del cart[food_id]

    request.session["cart"] = cart

    return redirect("cart")
def increase(request, food_id):

    cart = request.session.get("cart", {})

    food_id = str(food_id)

    if food_id in cart:
        cart[food_id]["quantity"] += 1

    request.session["cart"] = cart

    return redirect("cart")
def decrease(request, food_id):

    cart = request.session.get("cart", {})

    food_id = str(food_id)

    if food_id in cart:

        cart[food_id]["quantity"] -= 1

        if cart[food_id]["quantity"] <= 0:
            del cart[food_id]

    request.session["cart"] = cart

    return redirect("cart")