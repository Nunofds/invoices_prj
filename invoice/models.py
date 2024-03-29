from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
from django.utils import timezone
from uuid import uuid4
from django.contrib.auth.models import User


class Client(models.Model):
    """
    Name: Client model definition
    Description:
    Author: (Nuno Fernandes) n.fernandes.contact@gmail.com
    """

    PROVINCES = [
        ('Europe', 'Europe'),
        ('Afrique', 'Afrique'),
        ('Asie', 'Asie'),
        ('Amérique', 'Amérique'),
        ('Océanie', 'Océanie')
    ]

    # Basic fields
    clientName = models.CharField(null=True, blank=True, max_length=200)
    client_siret = models.CharField(null=True, blank=True, max_length=20)
    province = models.CharField(null=True, blank=True, max_length=100, choices=PROVINCES)
    addressLine1 = models.CharField(null=True, blank=True, max_length=200)
    city = models.CharField(null=True, blank=True, max_length=30)
    zip_code = models.CharField(null=True, blank=True, max_length=12)
    phone = models.CharField(null=True, blank=True, max_length=20)
    email = models.EmailField(null=True, blank=True, max_length=100)
    saved_by = models.ForeignKey(User, on_delete=models.PROTECT)

    # Utility fields
    uniqueId = models.CharField(null=True, blank=True, max_length=100)
    slug = models.SlugField(max_length=500, null=True, blank=True, unique=True)
    created_date = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        ordering = ['-clientName']
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'

    def __str__(self):
        return f"{self.clientName} {self.province} {self.uniqueId}"

    def get_absolute_url(self):
        return reverse('client-detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if self.created_date is None:
            self.created_date = timezone.localtime(timezone.now())
        if self.uniqueId is None:
            self.uniqueId = str(uuid4()).split('-')[4]
            self.slug = slugify(f"{self.clientName} {self.province} {self.uniqueId}")

        self.slug = slugify(f"{self.clientName} {self.province} {self.uniqueId}")
        self.last_update = timezone.localtime(timezone.now())

        super(Client, self).save(*args, **kwargs)

#
# class Invoice(models.Model):
#     """
#     Name: Invoice model definition
#     Description :
#     Author: (Nuno Fernandes) n.fernandes.contact@gmail.com
#     """
#
#     INVOICE_TYPE = (
#         ('R', 'RECU'),
#         ('P', 'PROFORMA FACTURE'),
#         ('F', 'FACTURE'),
#     )
#     customer = models.ForeignKey(Client, on_delete=models.PROTECT)
#     invoice_type = models.CharField(max_length=1, choices=INVOICE_TYPE)
#     # number = models.PositiveIntegerField(default=0)
#     invoice_date = models.DateTimeField(auto_now_add=True)
#     invoice_deadline = models.DateField()
#     total = models.DecimalField(max_digits=1000, decimal_places=2)
#     comments = models.TextField(null=True, blank='True', max_length=1000)
#     paid = models.BooleanField(default=False)
#     last_updated_date = models.DateTimeField(null=True, blank=True, auto_now=True)
#     saved_by = models.ForeignKey(User, on_delete=models.PROTECT)
#
#     class Meta:
#         ordering = ['-customer']
#         verbose_name = 'Invoice'
#         verbose_name_plural = 'Invoices'
#
#     def __str__(self):
#         return f"{self.customer.name}{self.invoice_date}"
#
#     @property
#     def get_total(self):
#         services = self.service_set.all()
#         total = sum(service.get_total for service in services)
#
#
# class Service(models.Model):
#     """
#     Name: Service model definition
#     Description: ...
#     Author: (Nuno Fernandes) n.fernandes.contact@gmail.com
#     """
#
#     name = models.CharField(max_length=100)
#     quantity = models.IntegerField(default=0)
#     unit_price = models.DecimalField(max_digits=1000, decimal_places=2)
#     total = models.DecimalField(max_digits=1000, decimal_places=2)
#     invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
#
#     class Meta:
#         ordering = ['-name']
#         verbose_name = 'Service'
#         verbose_name_plural = 'Services'
#
#     @property
#     def get_total(self):
#         total = self.quantity * self.unit_price
