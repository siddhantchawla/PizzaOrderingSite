# Generated by Django 2.0.3 on 2018-07-15 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0018_remove_order_pizza_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='topping_name',
            field=models.CharField(default=0, max_length=128),
        ),
    ]
