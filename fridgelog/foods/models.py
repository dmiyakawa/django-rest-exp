from django.db import models

FOOD_CATEGORIES = [
    (1, "飲み物"),
    (2, "食べ物"),
]

class Food(models.Model):
    name = models.CharField(max_length=15)
    owner_name = models.CharField(
        max_length=20, blank=True
    )
    owner_slack = models.CharField(
        max_length=20, blank=True
    )
    category = models.SmallIntegerField(
        choices=FOOD_CATEGORIES
    )
    expiration_date = models.DateField()

    def __str__(self):
        owner = self.owner_name or self.owner_slack
        return f"{self.name}({owner})"

