# Generated by Django 2.0.3 on 2018-07-14 09:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0017_order_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='pizza_id',
        ),
    ]
