# Generated by Django 3.2.15 on 2022-12-06 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_rename_photo_wick_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Back',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.IntegerField(verbose_name='Фото вверху')),
            ],
        ),
    ]
