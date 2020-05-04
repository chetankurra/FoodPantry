# Generated by Django 2.2.5 on 2020-05-03 22:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('provider', '0006_auto_20200503_1552'),
        ('inventory', '0006_remove_inventory_donor'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventory',
            name='donor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='donor', to='provider.provider'),
            preserve_default=False,
        ),
    ]
