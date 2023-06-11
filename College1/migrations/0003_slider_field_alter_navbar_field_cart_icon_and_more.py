# Generated by Django 4.1.7 on 2023-03-22 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('College1', '0002_navbar_field'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slider_Field',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caroasel_tag', models.TextField()),
                ('caroasel_image', models.ImageField(upload_to='static/image1/courasel_images/')),
                ('caroasel_text', models.CharField(max_length=40)),
            ],
        ),
        migrations.AlterField(
            model_name='navbar_field',
            name='cart_icon',
            field=models.ImageField(upload_to='static/image1/navbar/'),
        ),
        migrations.AlterField(
            model_name='navbar_field',
            name='login_icon',
            field=models.ImageField(upload_to='static/image1/navbar/'),
        ),
    ]