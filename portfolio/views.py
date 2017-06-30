from django.shortcuts import render
from django.views import generic
from .models import Company


# Create your views here.
class IndexView(generic.ListView):
    template_name = 'portfolio/index.html'

    def get_queryset(self):
        return Company.objects.all()

