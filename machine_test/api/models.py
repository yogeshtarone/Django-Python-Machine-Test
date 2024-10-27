from django.db import models


class Shoe(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    size = models.FloatField()
    color = models.CharField(max_length=50, default='Unknown')
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

