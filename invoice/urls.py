from django.urls import path, include

from . import views

app_name = 'invoice'

urlpatterns = ([
    path('login/', views.login, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
])
