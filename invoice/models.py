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
    clientLogo = models.ImageField(default='default_logo.jpg', upload_to='company_logos')
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


class Invoice(models.Model):
    """
    Name: Invoice model definition
    Description :
    Author: (Nuno Fernandes) n.fernandes.contact@gmail.com
    """

    TERMS = (
        ('14 days', '14 days'),
        ('30 days', '30 days'),
        ('60 days', '60 days'),
    )

    STATUS = [
        ('CURRENT', 'CURRENT'),
        ('OVERDUE', 'OVERDUE'),
        ('PAID', 'PAID'),
    ]

    title = models.CharField(max_length=100, null=True, blank=True)
    number = models.CharField(max_length=100, null=True, blank=True)
    due_date = models.DateField(null=True, blank=True)
    payment_terms = models.DateField(null=True, blank=True, choices=TERMS, default='14 days')
    status = models.CharField(null=True, blank=True, choices=STATUS)
    notes = models.TextField(null=True, blank='True')
    saved_by = models.ForeignKey(User, on_delete=models.PROTECT)

    # Related fields
    client = models.ForeignKey(Client, blank=True, null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey('Product', blank=True, null=True, on_delete=models.SET_NULL)

    # Utility fields
    uniqueId = models.CharField(null=True, blank=True, max_length=100)
    slug = models.CharField(null=True, blank=True, max_length=500, unique=True)
    created_date = models.DateTimeField(blank=True, auto_now_add=True)
    last_update = models.DateTimeField(blank=True, null=True, auto_now=True)





    class Meta:
        ordering = ['-customer']
        verbose_name = 'Invoice'
        verbose_name_plural = 'Invoices'

    def __str__(self):
        return f"{self.customer.name}{self.invoice_date}"


class Product(models.Model):
    """
    Name: Product model definition
    Description: ...
    Author: (Nuno Fernandes) n.fernandes.contact@gmail.com
    """

    CURRENCY = [
        ('€', 'EUR'),
        ('$', 'USD'),
    ]

    # Base fields
    title = models.CharField(null=True, blank=True, max_length=100)
    description = models.TextField(null=True, blank=True)
    quantity = models.FloatField(null=True, blank=True)
    price = models.FloatField(null=True, blank=True)
    currency = models.CharField(choices=CURRENCY, default='€', max_length=1)

    # Utility fields
    uniqueId = models.CharField(null=True, blank=True, max_length=100)
    slug = models.CharField(null=True, blank=True, max_length=500, unique=True)
    created_date = models.DateTimeField(blank=True, auto_now_add=True)
    last_update = models.DateTimeField(blank=True, null=True, auto_now=True)

    class Meta:
        ordering = ['-title']
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return f"{self.title} {self.uniqueId}"

    def get_absolute_url(self):
        return reverse('invoice-detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if self.created_date is None:
            self.created_date = timezone.localtime(timezone.now())
        if self.uniqueId is None:
            self.uniqueId = str(uuid4()).split('-')[4]
            self.slug = slugify(f"{self.title} {self.currency} {self.uniqueId}")

        self.slug = slugify(f"{self.title} {self.currency} {self.uniqueId}")
        self.last_update = timezone.localtime(timezone.now())

        super(Product, self).save(*args, **kwargs)
