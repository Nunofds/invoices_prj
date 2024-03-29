from django.urls import path, include

from . import views

app_name = 'invoice'

urlpatterns = ([
    path('invoices/', views.invoices, name='invoices')
])
