from django.conf.urls import url
from . import views

app_name = 'portfolio'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name = 'index'),

    url(r'company/add/$', views.CompanyCreate.as_view(), name = "company-add"),

    url(r'company/add-stock/$', views.StockCreate.as_view(), name = "stock-add"),

    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name = 'detail'),

    url(r'company/(?P<pk>[0-9]+)/delete/$', views.CompanyDelete.as_view(), name = 'company-delete'),
]
