# Generated by Django 5.0.4 on 2024-04-25 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0020_remove_offer_offer_terms'),
    ]

    operations = [
        migrations.AddField(
            model_name='offer',
            name='offers',
            field=models.IntegerField(default=0, help_text='Discount on the restaurant in percentage'),
        ),
    ]
