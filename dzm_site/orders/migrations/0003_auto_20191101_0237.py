# Generated by Django 2.2.6 on 2019-11-01 02:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20191030_1725'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productinorder',
            old_name='price_item',
            new_name='price_per_item',
        ),
    ]
