# Generated by Django 4.1.7 on 2023-04-02 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('College1', '0010_contact_model_alter_about_team_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Login_Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='static/image1/login_page/')),
            ],
        ),
    ]
