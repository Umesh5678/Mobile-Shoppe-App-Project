# Generated by Django 4.1.7 on 2023-04-24 02:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('College1', '0020_cart_model'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart_model',
            name='product_quantity',
        ),
    ]
