# Generated by Django 2.2.6 on 2019-10-30 17:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='imageproduct',
            options={'verbose_name': 'Image of product', 'verbose_name_plural': 'Images of products'},
        ),
    ]
