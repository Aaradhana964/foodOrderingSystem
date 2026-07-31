from django.urls import path
from . import views

urlpatterns = [

    path(
        "",
        views.menu_list,
        name="menu"
    ),

    path(
        "<int:pk>/",
        views.food_detail,
        name="food_detail"
    ),

    path(
        "add/",
        views.add_food,
        name="add_food"
    ),

]
