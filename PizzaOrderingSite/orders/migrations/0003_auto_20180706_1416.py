# Generated by Django 2.0.3 on 2018-07-06 14:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20180706_1413'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pizza',
            name='pizza',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='orders.Type'),
        ),
    ]
