from django.urls import path
from . import views

urlpatterns = [

    path("", views.cart, name="cart"),

    path("add/<int:food_id>/", views.add_to_cart, name="add_to_cart"),

    path("remove/<int:food_id>/", views.remove_item, name="remove_item"),

    path("increase/<int:food_id>/", views.increase, name="increase"),

    path("decrease/<int:food_id>/", views.decrease, name="decrease"),

]