# Generated by Django 5.0 on 2024-07-16 22:43

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coursier', '0002_rename_courier_coursier'),
    ]

    operations = [
        migrations.AddField(
            model_name='coursier',
            name='date_naissance',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='coursier',
            name='lieu_naissance',
            field=models.CharField(default=django.utils.timezone.now, max_length=150),
            preserve_default=False,
        ),
    ]
