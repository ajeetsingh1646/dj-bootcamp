# Generated by Django 3.1.7 on 2021-04-17 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_product_can_backorder'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='video_link',
            field=models.TextField(blank=True, null=True),
        ),
    ]
