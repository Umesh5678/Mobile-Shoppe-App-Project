# Generated by Django 4.1.7 on 2023-04-08 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('College1', '0013_popup_model'),
    ]

    operations = [
        migrations.AddField(
            model_name='mobile_model',
            name='product_brand',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.DeleteModel(
            name='Popup_Model',
        ),
    ]
