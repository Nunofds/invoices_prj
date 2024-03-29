from django.contrib import admin

from .models import Client


class AdminClient(admin.ModelAdmin):
    list_display = (
        'clientName', 'client_siret', 'phone', 'email', 'province', 'addressLine1', 'city', 'zip_code', 'created_date',
        'last_update', 'saved_by')


# class AdminInvoice(admin.ModelAdmin):
#     list_display = (
#         'customer', 'invoice_date', 'invoice_deadline', 'last_updated_date', 'paid', 'comments', 'total',
#         'saved_by',
#     )
#
#
# class AdminService(admin.ModelAdmin):
#     list_display = ('name', 'quantity', 'unit_price', 'total', 'invoice')


admin.site.register(Client, AdminClient)
# admin.site.register(Invoice, AdminInvoice)
# admin.site.register(Service, AdminService)
