# Generated by Django 5.0.6 on 2024-07-18 14:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_remove_product_quantity_product_picture_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='products',
            field=models.ManyToManyField(null=True, related_name='categories', to='orders.product'),
        ),
        migrations.AlterField(
            model_name='product',
            name='command',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='orders.command'),
        ),
    ]
