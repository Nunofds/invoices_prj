from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    """
    Name: Customer model definition
    Description:
    Author: (Nuno Fernandes) n.fernandes.contact@gmail.com
    """

    name = models.CharField(verbose_name='Nom d\'utilisateur', max_length=132)
    email = models.EmailField(verbose_name='Email')
    phone = models.CharField(verbose_name='Telephone')
    address = models.CharField(verbose_name='Adresse ', max_length=100)
    city = models.CharField(verbose_name='Ville', max_length=100)
    zip_code = models.CharField(verbose_name='Code postal', max_length=20)
    siret = models.PositiveIntegerField(verbose_name='SIRET')
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

    number = models.PositiveIntegerField(verbose_name='Numéro de facture')
    total = models.DecimalField(verbose_name='Total', max_digits=9999999, decimal_places=2)
    invoice_date = models.DateTimeField(verbose_name='Date', auto_now_add=True)
    invoice_deadline = models.DateField(verbose_name="Échéance")
    last_updated_date = models.DateTimeField(verbose_name='Date de dernière mise à jour', null=True, blank=True)
    paid = models.BooleanField(verbose_name="Payé", default=False)
    invoice_type = models.CharField(verbode_name='Type de facture', max_length=1, choices=INVOICE_TYPE)
    comments = models.TextField(verbose_name='Commentaire', null=True, blank='True', max_length=1000)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    saved_by = models.ForeignKey(User, on_delete=models.PROTECT)

    class Meta:
        ordering = ['-number']
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

    name = models.CharField(verbose_name='Nom', max_length=100)
    quantity = models.IntegerField(verbose_name='Quantité', default=0)
    unit_price = models.DecimalField(verbose_name='Prix unité', max_digits=1000, decimal_places=2)
    total = models.DecimalField(verbose_name='Total', max_digits=1000, decimal_places=2)
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-name']
        verbose_name = 'Service'
        verbose_name_plural = 'Services'

    @property
    def get_total(self):
        total = self.quantity * self.unit_price
