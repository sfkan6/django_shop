# Generated by Django 4.0.6 on 2022-08-03 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=7, null=True, verbose_name='Цена'),
        ),
    ]
