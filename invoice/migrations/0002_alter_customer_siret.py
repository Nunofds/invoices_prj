# Generated by Django 5.0.3 on 2024-03-29 00:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='siret',
            field=models.CharField(max_length=20),
        ),
    ]
