from django.contrib import admin

from .models import Invoice, Customer, Service

admin.site.register(Customer)
admin.site.register(Invoice)
admin.site.register(Service)
