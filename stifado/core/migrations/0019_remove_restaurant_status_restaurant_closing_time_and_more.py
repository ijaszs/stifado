# Generated by Django 5.0.4 on 2024-04-25 04:49

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0018_delete_cart'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restaurant',
            name='status',
        ),
        migrations.AddField(
            model_name='restaurant',
            name='closing_time',
            field=models.TimeField(default=datetime.datetime(2024, 4, 25, 22, 0, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='opening_time',
            field=models.TimeField(default=datetime.datetime(2024, 4, 25, 9, 0, tzinfo=datetime.timezone.utc)),
        ),
        migrations.CreateModel(
            name='OpeningHours',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day_of_week', models.IntegerField()),
                ('open_time', models.TimeField()),
                ('close_time', models.TimeField()),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='opening_hours', to='core.restaurant')),
            ],
        ),
    ]