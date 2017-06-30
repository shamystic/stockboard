from django.contrib import admin
from .models import Stock, Company # .models is models file in current directory


# Register your models here.
admin.site.register(Company)

admin.site.register(Stock)

