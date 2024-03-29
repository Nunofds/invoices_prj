from django.contrib import admin

from .models import Client, Product, Invoice, Settings


class AdminClient(admin.ModelAdmin):
    list_display = (
        'clientName', 'client_siret', 'phone', 'email', 'province', 'addressLine1', 'city', 'zip_code', 'created_date',
        'last_update', 'saved_by')


class AdminInvoice(admin.ModelAdmin):
    list_display = (
        'client', 'title', 'number', 'created_date', 'due_date', 'last_update', 'status', 'payment_terms', 'notes',
        'saved_by',
    )


class AdminProduct(admin.ModelAdmin):
    list_display = (
        'title', 'description', 'quantity', 'currency', 'price', 'created_date', 'slug', 'last_update'
    )


class AdminSettings(admin.ModelAdmin):
    list_display = (
        'clientName', 'client_siret', 'phone', 'email', 'province', 'addressLine1', 'city', 'zip_code', 'created_date',
        'last_update', 'saved_by')


admin.site.register(Client, AdminClient)
admin.site.register(Product, AdminProduct)
admin.site.register(Invoice, AdminInvoice)
admin.site.register(Settings, AdminSettings)
