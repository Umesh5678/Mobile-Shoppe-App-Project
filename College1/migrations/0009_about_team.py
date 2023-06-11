# Generated by Django 4.1.7 on 2023-04-02 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('College1', '0008_about_model'),
    ]

    operations = [
        migrations.CreateModel(
            name='About_team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='static/image1/about_page/team_images')),
                ('name', models.CharField(max_length=25)),
                ('description', models.CharField(max_length=50)),
            ],
        ),
    ]
