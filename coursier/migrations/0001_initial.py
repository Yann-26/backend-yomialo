# Generated by Django 5.0 on 2024-07-12 16:08

import coursier.models
import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Courier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quarier', models.CharField(max_length=120)),
                ('phone_number', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=255)),
                ('recto_card_image', models.ImageField(upload_to=coursier.models.user_directory_path)),
                ('verso_card_image', models.ImageField(upload_to=coursier.models.user_directory_path)),
                ('selfie_image', models.ImageField(upload_to=coursier.models.user_directory_path)),
                ('is_verified', models.BooleanField(default=False)),
                ('auth_token', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]