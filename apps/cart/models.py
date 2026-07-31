from django.db import models
from django.conf import settings
from apps.menu.models import Food


class Cart(models.Model):

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    food = models.ForeignKey(
        Food,
        on_delete=models.CASCADE
    )

    quantity = models.PositiveIntegerField(default=1)

    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.food.name}"