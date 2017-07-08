from django.contrib import admin
from .models import Stock, Company, Excel # .models is models file in current directory


# Register your models here.
admin.site.register(Excel)

admin.site.register(Company)

admin.site.register(Stock)

