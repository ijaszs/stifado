# Generated by Django 5.0.2 on 2024-03-12 04:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='prodect',
            old_name='name',
            new_name='title',
        ),
    ]