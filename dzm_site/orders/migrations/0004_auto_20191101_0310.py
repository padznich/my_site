# Generated by Django 2.2.6 on 2019-11-01 03:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_auto_20191101_0237'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productinorder',
            old_name='total_amount',
            new_name='total_price',
        ),
    ]
