from django.db import models
from django.conf import settings

from apps.menu.models import Food


class Order(models.Model):

    STATUS_CHOICES = (
        ("Pending", "Pending"),
        ("Confirmed", "Confirmed"),
        ("Preparing", "Preparing"),
        ("Delivery", "Delivery"),
        ("Delivered", "Delivered"),
        ("Cancelled", "Cancelled"),
    )

    PAYMENT_CHOICES = (
        ("Pending", "Pending"),
        ("Paid", "Paid"),
    )

    PAYMENT_METHOD_CHOICES = (
        ("COD", "Cash on Delivery"),
    )


    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    total_amount = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    delivery_address = models.TextField()


    status = models.CharField(
        max_length=30,
        choices=STATUS_CHOICES,
        default="Pending"
    )


    payment_method = models.CharField(
        max_length=20,
        choices=PAYMENT_METHOD_CHOICES,
        default="COD"
    )


    payment_status = models.CharField(
        max_length=20,
        choices=PAYMENT_CHOICES,
        default="Pending"
    )


    ordered_at = models.DateTimeField(
        auto_now_add=True
    )


    def __str__(self):
        return f"Order #{self.id}"



class OrderItem(models.Model):

    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name="items"
    )

    food = models.ForeignKey(
        Food,
        on_delete=models.CASCADE
    )

    quantity = models.PositiveIntegerField()

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )


    def subtotal(self):
        return self.quantity * self.price