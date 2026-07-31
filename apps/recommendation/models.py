from django.db import models


class Recommendation(models.Model):

    GOALS = (
        ("Weight Loss", "Weight Loss"),
        ("Weight Gain", "Weight Gain"),
        ("Maintain Weight", "Maintain Weight"),
    )

    goal = models.CharField(max_length=30, choices=GOALS)

    budget = models.DecimalField(max_digits=8, decimal_places=2)

    cuisine = models.CharField(max_length=100)

    recommended_food = models.CharField(max_length=150)

    calories = models.IntegerField()

    protein = models.IntegerField()

    carbs = models.IntegerField()

    fats = models.IntegerField()

    def __str__(self):
        return self.recommended_food