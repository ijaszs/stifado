# Generated by Django 5.0.2 on 2024-03-03 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='prodect',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('price', models.FloatField()),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='uplodes')),
                ('priority', models.IntegerField(default=0)),
                ('delete_status', models.IntegerField(choices=[(1, 'live'), (0, 'delete')], default='live')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('upadated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]