# Generated by Django 4.1.7 on 2023-03-22 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('College1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Navbar_Field',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sitelogo', models.CharField(max_length=15)),
                ('nav_field_1', models.CharField(max_length=15)),
                ('nav_field_2', models.CharField(max_length=15)),
                ('nav_field_3', models.CharField(max_length=15)),
                ('nav_field_4', models.CharField(max_length=15)),
                ('nav_field_5', models.CharField(max_length=15)),
                ('nav_field_6', models.CharField(max_length=15)),
                ('nav_field_7', models.CharField(max_length=15)),
                ('login_icon', models.ImageField(upload_to='static/')),
                ('cart_icon', models.ImageField(upload_to='static/')),
            ],
        ),
    ]