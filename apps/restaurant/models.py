from django.db import models


class Restaurant(models.Model):

    name = models.CharField(max_length=150)

    owner = models.CharField(max_length=100)

    image = models.ImageField(upload_to="restaurants/")

    location = models.CharField(max_length=200)

    cuisine = models.CharField(max_length=100)

    description = models.TextField()

    rating = models.DecimalField(max_digits=2, decimal_places=1, default=4.5)

    opening_time = models.TimeField()

    closing_time = models.TimeField()

    is_open = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name