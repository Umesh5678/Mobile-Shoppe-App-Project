# Generated by Django 4.1.7 on 2023-04-02 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('College1', '0004_brands_model'),
    ]

    operations = [
        migrations.CreateModel(
            name='Footer_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('textfield', models.CharField(max_length=200)),
                ('services', models.CharField(max_length=50)),
            ],
        ),
    ]
