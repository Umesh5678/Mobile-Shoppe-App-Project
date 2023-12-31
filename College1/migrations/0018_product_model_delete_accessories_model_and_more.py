# Generated by Django 4.1.7 on 2023-04-23 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('College1', '0017_accessories_model'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product_Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_type', models.CharField(max_length=20, null=True)),
                ('product_image', models.ImageField(upload_to='static/image1/mobile_images/')),
                ('product_name', models.CharField(max_length=50)),
                ('product_rate', models.FloatField()),
                ('product_color', models.CharField(max_length=20, null=True)),
                ('product_description', models.TextField(null=True)),
                ('product_info', models.TextField(null=True)),
                ('product_policy', models.TextField(null=True)),
                ('product_shipping', models.TextField(null=True)),
                ('product_feature1', models.CharField(max_length=100, null=True)),
                ('product_feature2', models.CharField(max_length=100, null=True)),
                ('product_feature3', models.CharField(max_length=100, null=True)),
                ('product_feature4', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Accessories_Model',
        ),
        migrations.DeleteModel(
            name='Mobile_Model',
        ),
        migrations.DeleteModel(
            name='Tablet_Model',
        ),
    ]
