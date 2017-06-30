from django.contrib import admin
from .models import Stock # .models is models file in current directory


# Register your models here.
admin.site.register(Stock)
