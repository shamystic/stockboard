from django.db import models

# Create your models here.


class Stock(models.Model):
    ticker = models.CharField(max_length=250)
    price_paid = models.FloatField()
    quantity = models.FloatField()

    def __str__(self):  # gives string representation of the object!
        return self.ticker