from django.db import models
from apps.restaurant.models import Restaurant


class Category(models.Model):

    name = models.CharField(max_length=100)

    image = models.ImageField(upload_to="categories/")

    def __str__(self):
        return self.name


class Food(models.Model):

    restaurant = models.ForeignKey(
        Restaurant,
        on_delete=models.CASCADE,
        related_name="foods"
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE
    )

    name = models.CharField(max_length=150)

    image = models.CharField(max_length=200)

    description = models.TextField()

    price = models.DecimalField(max_digits=8, decimal_places=2)

    is_veg = models.BooleanField(default=True)

    available = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name