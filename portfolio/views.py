from django.shortcuts import render
from django.views import generic
from .models import Company, Stock, Excel
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, DeleteView
from django.core.urlresolvers import reverse_lazy



# Create your views here.
class IndexView(TemplateView):
    template_name = 'portfolio/index.html'

    def get_queryset(self):
        return Company.objects.all()

class PortfolioView(generic.ListView):
    template_name = 'portfolio/pv.html'

    def get_queryset(self):
        return Excel.objects.all()

class AnalyticView(generic.ListView):
    template_name = 'portfolio/analytics.html'

    def get_queryset(self):
        return Company.objects.all()

class DetailView(generic.DetailView):
    model = Company
    template_name = 'portfolio/detail.html'

class ExcelAdd(CreateView):
    model = Excel
    fields = ['portfolio_file']

class CompanyCreate(CreateView):
    model = Company
    # attributes we need from the user
    fields = ['ticker']

class CompanyDelete(DeleteView):
    model = Company
    success_url = reverse_lazy('portfolio:pv') #redirect to here after delete

class StockCreate(CreateView):
    model = Stock
    fields = ['company', 'price_paid', 'quantity']
