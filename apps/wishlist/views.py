from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Wishlist
from apps.menu.models import Food


@login_required
def add_to_wishlist(request, item_id):

    food = get_object_or_404(
        Food,
        id=item_id
    )

    Wishlist.objects.get_or_create(
        user=request.user,
        food=food
    )

    return redirect(
        request.META.get(
            "HTTP_REFERER",
            "/"
        )
    )


@login_required
def remove_from_wishlist(request, item_id):

    food = get_object_or_404(
        Food,
        id=item_id
    )

    Wishlist.objects.filter(
        user=request.user,
        food=food
    ).delete()

    return redirect(
        request.META.get(
            "HTTP_REFERER",
            "/"
        )
    )


@login_required
def wishlist_view(request):

    wishlist_items = Wishlist.objects.filter(
        user=request.user
    ).select_related(
        "food"
    )

    return render(
        request,
        "wishlist/wishlist.html",
        {
            "wishlist_items": wishlist_items
        }
    )