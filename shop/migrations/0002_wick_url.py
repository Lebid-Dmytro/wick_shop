# Generated by Django 3.2.15 on 2022-12-06 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='wick',
            name='url',
            field=models.SlugField(default=True, max_length=130),
        ),
    ]
