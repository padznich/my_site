# Generated by Django 2.2.6 on 2019-11-06 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_product_discount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imageproduct',
            name='image',
            field=models.ImageField(upload_to='products_images/'),
        ),
    ]