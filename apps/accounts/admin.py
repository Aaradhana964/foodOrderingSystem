from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ("Profile Information", {
            "fields": (
                "phone",
                "address",
                "profile_image",
            )
        }),
    )