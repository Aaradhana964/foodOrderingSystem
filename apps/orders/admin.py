from django.contrib import admin
from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):

    model = OrderItem
    extra = 0



# Change order status actions

@admin.action(description="Confirm selected orders")
def confirm_orders(modeladmin, request, queryset):
    queryset.update(status="Confirmed")


@admin.action(description="Start preparing selected orders")
def preparing_orders(modeladmin, request, queryset):
    queryset.update(status="Preparing")


@admin.action(description="Mark as out for delivery")
def out_for_delivery(modeladmin, request, queryset):
    queryset.update(status="Out for Delivery")


@admin.action(description="Mark as delivered")
def delivered_orders(modeladmin, request, queryset):
    queryset.update(status="Delivered")


@admin.action(description="Mark payment as received")
def payment_received(modeladmin, request, queryset):
    queryset.update(payment_status="Paid")



@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "user",
        "status",
        "payment_method",
        "payment_status",
        "total_amount",
        "ordered_at",
    )

    inlines = [
        OrderItemInline
    ]

    actions = [
        confirm_orders,
        preparing_orders,
        out_for_delivery,
        delivered_orders,
        payment_received,
    ]