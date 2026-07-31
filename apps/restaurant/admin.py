from django.contrib import admin
from .models import Restaurant


@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "location",
        "cuisine",
        "rating",
        "is_open",
    )

    search_fields = (
        "name",
        "location",
        "cuisine",
    )

    list_filter = (
        "cuisine",
        "is_open",
    )