# Generated by Django 3.2.15 on 2022-12-06 16:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_alter_wick_url'),
    ]

    operations = [
        migrations.RenameField(
            model_name='wick',
            old_name='photo',
            new_name='image',
        ),
    ]
