from django.contrib import admin

from .models import Invoice, Customer, Service


class AdminCustomer(admin.ModelAdmin):
    list_display = (
        'name', 'email', 'phone', 'address', 'city', 'zip_code', 'siret', 'created_date', 'updated_date', 'saved_by')


class AdminInvoice(admin.ModelAdmin):
    list_display = (
        'customer', 'invoice_date', 'invoice_deadline', 'last_updated_date', 'paid', 'comments', 'total',
        'saved_by',
    )


class AdminService(admin.ModelAdmin):
    list_display = ('name', 'quantity', 'unit_price', 'total', 'invoice')


admin.site.register(Customer, AdminCustomer)
admin.site.register(Invoice, AdminInvoice)
admin.site.register(Service, AdminService)
