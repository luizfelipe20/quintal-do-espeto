# Generated by Django 5.0.6 on 2024-06-10 03:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_table_alter_order_availability'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='table',
        ),
        migrations.AddField(
            model_name='order',
            name='_table',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.table', verbose_name='Mesa'),
        ),
    ]