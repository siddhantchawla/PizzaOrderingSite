# Generated by Django 2.0.3 on 2018-07-07 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0009_auto_20180707_0742'),
    ]

    operations = [
        migrations.AddField(
            model_name='pizza',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
        ),
    ]
