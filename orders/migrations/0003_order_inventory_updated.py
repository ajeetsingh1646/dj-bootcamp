# Generated by Django 3.1.7 on 2021-04-07 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20210403_0403'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='inventory_updated',
            field=models.BooleanField(default=False),
        ),
    ]
