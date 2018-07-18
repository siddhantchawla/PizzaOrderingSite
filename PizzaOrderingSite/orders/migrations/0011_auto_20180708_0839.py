# Generated by Django 2.0.3 on 2018-07-08 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0010_pizza_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='subtotal',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=12),
        ),
        migrations.AddField(
            model_name='order',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]