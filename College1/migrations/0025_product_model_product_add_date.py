# Generated by Django 4.1.7 on 2023-04-26 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('College1', '0024_contact_response_model'),
    ]

    operations = [
        migrations.AddField(
            model_name='product_model',
            name='product_add_date',
            field=models.DateField(null=True),
        ),
    ]
