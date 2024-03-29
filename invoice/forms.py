from django import forms
from django.contrib.auth.models import User
from django.forms import widgets

from .models import *
import json


class UserLoginForm(forms.ModelForm):
    """
    Name: User Form Definition (Extends by default User model in Django)
    Description:
    Author: (Nuno Fernandes) n.fernandes.contact@gmail.com
    """

    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class ClientForm(forms.ModelForm):
    """
    Name: Client Form Definition
    Description:
    Author: (Nuno Fernandes) n.fernandes.contact@gmail.com
    """

    class Meta:
        model = Client
        fields = ['clientName', 'client_siret', 'clientLogo', 'province', 'addressLine1', 'city', 'zip_code', 'phone',
                  'email', 'taxNumber', 'saved_by']


class ProductForm(forms.ModelForm):
    """
    Name: Product Form Definition
    Description:
    Author: (Nuno Fernandes) n.fernandes.contact@gmail.com
    """

    class Meta:
        model = Product
        fields = ['title', 'description', 'quantity', 'price', 'currency']


class InvoiceForm(forms.ModelForm):
    """
    Name: Invoice Form Definition
    Description:
    Author: (Nuno Fernandes) n.fernandes.contact@gmail.com
    """

    class Meta:
        model = Invoice
        fields = ['title', 'number', 'due_date', 'payment_terms', 'status', 'notes', 'client', 'product', 'saved_by']


class SettingsForm(forms.ModelForm):
    """
    Name: Settings Form Definition
    Description:
    Author: (Nuno Fernandes) n.fernandes.contact@gmail.com
    """

    class Meta:
        model = Settings
        fields = ['clientName', 'client_siret', 'clientLogo', 'province', 'addressLine1', 'city', 'zip_code', 'phone',
                  'email', 'taxNumber', 'saved_by']
