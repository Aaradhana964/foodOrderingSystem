from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):

    phone = models.CharField(
        max_length=15,
        blank=True
    )

    address = models.TextField(
        blank=True
    )

    profile_image = models.ImageField(
        upload_to="profiles/",
        blank=True,
        null=True
    )


    def __str__(self):
        return self.username