from django.shortcuts import render
from django.views import generic
from .models import Stock


# Create your views here.
class IndexView(generic.ListView):
    template_name = 'portfolio/index.html'
    context_object_name = 'stocks'

    def get_queryset(self):
        return Stock.objects.all()

