# Generated by Django 5.0.6 on 2024-06-10 02:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_order_availability_order_cliente_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='cliente',
            new_name='client',
        ),
    ]
