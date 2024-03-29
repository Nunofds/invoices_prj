# Generated by Django 5.0.3 on 2024-03-29 15:57

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0007_alter_invoice_status'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='taxNumber',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clientName', models.CharField(blank=True, max_length=200, null=True)),
                ('client_siret', models.CharField(blank=True, max_length=20, null=True)),
                ('clientLogo', models.ImageField(default='default_logo.jpg', upload_to='company_logos')),
                ('province', models.CharField(blank=True, choices=[('Europe', 'Europe'), ('Afrique', 'Afrique'), ('Asie', 'Asie'), ('Amérique', 'Amérique'), ('Océanie', 'Océanie')], max_length=100, null=True)),
                ('addressLine1', models.CharField(blank=True, max_length=200, null=True)),
                ('city', models.CharField(blank=True, max_length=30, null=True)),
                ('zip_code', models.CharField(blank=True, max_length=12, null=True)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('email', models.EmailField(blank=True, max_length=100, null=True)),
                ('taxNumber', models.CharField(blank=True, max_length=100, null=True)),
                ('uniqueId', models.CharField(blank=True, max_length=100, null=True)),
                ('slug', models.SlugField(blank=True, max_length=500, null=True, unique=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('last_update', models.DateTimeField(auto_now=True, null=True)),
                ('saved_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Setting',
                'verbose_name_plural': 'Settings',
                'ordering': ['-clientName'],
            },
        ),
    ]