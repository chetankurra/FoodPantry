# Generated by Django 2.2.5 on 2020-05-03 04:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0003_auto_20200502_2118'),
    ]

    operations = [
        migrations.RenameField(
            model_name='checkout',
            old_name='inventory',
            new_name='item_in_inventory',
        ),
    ]