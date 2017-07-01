from django.shortcuts import render
from django.views import generic
from .models import Company, Stock
from django.views.generic.edit import CreateView


# Create your views here.
class IndexView(generic.ListView):
    template_name = 'portfolio/index.html'

    def get_queryset(self):
        return Company.objects.all()

class DetailView(generic.DetailView):
    model = Company
    template_name = 'portfolio/detail.html'

class CompanyCreate(CreateView):
    model = Company
    # attributes we need from the user
    fields = ['ticker']

class StockCreate(CreateView):
    model = Stock
    # attributes we need from the user
    fields = ['company', 'price_paid', 'quantity']
