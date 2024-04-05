from django.urls import path, include

from . import views

app_name = 'invoice'

urlpatterns = ([
    path('login/', views.login, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/invoices', views.invoices, name='invoices'),
    path('dashboard/productsOrServices', views.products_or_services, name='products_or_services'),
    path('dashboard/clients', views.clients, name='clients'),
])
