# Generated by Django 5.0.2 on 2024-03-24 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_product_restaurant_delete_user_product_restaurant'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='delivery_time',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
