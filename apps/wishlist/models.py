from django.db import models
from django.conf import settings
from apps.menu.models import Food


class Wishlist(models.Model):

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    food = models.ForeignKey(
        Food,
        on_delete=models.CASCADE
    )

    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        unique_together = ("user", "food")
        ordering = ["-created_at"]



    def __str__(self):
        return f"{self.user.username} - {self.food.name}"