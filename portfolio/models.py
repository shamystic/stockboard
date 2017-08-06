from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.

class Excel(models.Model): 
    portfolio_file = models.FileField()


class Company(models.Model):
    ticker = models.CharField(max_length=250, unique=True)

    def __str__(self):  # gives string representation of the object!
        return self.ticker

    def get_absolute_url(self):
        return reverse('portfolio:detail', kwargs = {'pk' : self.pk})

class Stock(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    price_paid = models.FloatField()
    quantity = models.FloatField() 

    def __str__(self):  # gives string representation of the object!
        return self.price_paid + '-' + self.quantity

    def get_absolute_url(self, company):
        return reverse('portfolio:index')
