# Generated by Django 5.0 on 2024-07-12 14:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0002_remove_produits_pharmaceutiques_assurances_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='verificationcode',
            name='user',
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
        migrations.DeleteModel(
            name='VerificationCode',
        ),
    ]
