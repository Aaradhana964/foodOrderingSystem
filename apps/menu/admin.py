from django.contrib import admin
from .models import Category, Food


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    list_display = ("name",)


@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "restaurant",
        "category",
        "price",
        "is_veg",
        "available"
    )

    list_filter = (
        "category",
        "restaurant",
        "is_veg",
        "available"
    )

    search_fields = (
        "name",
        "restaurant__name"
    )
