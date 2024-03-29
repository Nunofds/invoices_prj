from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    """
    Name: Customer model definition
    Description:
    Author: (Nuno Fernandes) n.fernandes.contact@gmail.com
    """

    name = models.CharField(max_length=132)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=20)
    siret = models.CharField(max_length=20)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    saved_by = models.ForeignKey(User, on_delete=models.PROTECT)

    class Meta:
        ordering = ['-name']
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'

    def __str__(self):
        return self.name


class Invoice(models.Model):
    """
    Name: Invoice model definition
    Description :
    Author: (Nuno Fernandes) n.fernandes.contact@gmail.com
    """

    INVOICE_TYPE = (
        ('R', 'RECU'),
        ('P', 'PROFORMA FACTURE'),
        ('F', 'FACTURE'),
    )
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    invoice_type = models.CharField(max_length=1, choices=INVOICE_TYPE)
    # number = models.PositiveIntegerField(default=0)
    invoice_date = models.DateTimeField(auto_now_add=True)
    invoice_deadline = models.DateField()
    total = models.DecimalField(max_digits=9999999, decimal_places=2)
    comments = models.TextField(null=True, blank='True', max_length=1000)
    paid = models.BooleanField(default=False)
    last_updated_date = models.DateTimeField(null=True, blank=True, auto_now=True)
    saved_by = models.ForeignKey(User, on_delete=models.PROTECT)

    class Meta:
        ordering = ['-customer']
        verbose_name = 'Invoice'
        verbose_name_plural = 'Invoices'

    def __str__(self):
        return f"{self.customer.name}{self.invoice_date}"

    @property
    def get_total(self):
        services = self.service_set.all()
        total = sum(service.get_total for service in services)


class Service(models.Model):
    """
    Name: Service model definition
    Description: ...
    Author: (Nuno Fernandes) n.fernandes.contact@gmail.com
    """

    name = models.CharField(max_length=100)
    quantity = models.IntegerField(default=0)
    unit_price = models.DecimalField(max_digits=1000, decimal_places=2)
    total = models.DecimalField(max_digits=1000, decimal_places=2)
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-name']
        verbose_name = 'Service'
        verbose_name_plural = 'Services'

    @property
    def get_total(self):
        total = self.quantity * self.unit_price
