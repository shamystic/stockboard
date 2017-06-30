from django.db import models

# Create your models here.


class Company(models.Model):
    ticker = models.CharField(max_length=250)

    def __str__(self):  # gives string representation of the object!
        return self.ticker

class Stock(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    price_paid = models.FloatField()
    quantity = models.FloatField()

    def __str__(self):
        return self.company