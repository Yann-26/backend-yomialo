# Generated by Django 5.0 on 2024-07-12 11:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produits_pharmaceutiques',
            name='assurances',
        ),
        migrations.RemoveField(
            model_name='pharmacies',
            name='assurances',
        ),
        migrations.RemoveField(
            model_name='produits_pharmaceutiques',
            name='la_categorie',
        ),
        migrations.RemoveField(
            model_name='ville',
            name='le_pays',
        ),
        migrations.RemoveField(
            model_name='pharmacies',
            name='le_pays',
        ),
        migrations.RemoveField(
            model_name='pharmacies',
            name='villes',
        ),
        migrations.RemoveField(
            model_name='produits_pharmaceutiques',
            name='la_pharmacies',
        ),
        migrations.DeleteModel(
            name='assurance',
        ),
        migrations.DeleteModel(
            name='Categorie',
        ),
        migrations.DeleteModel(
            name='Pays',
        ),
        migrations.DeleteModel(
            name='Ville',
        ),
        migrations.DeleteModel(
            name='pharmacies',
        ),
        migrations.DeleteModel(
            name='produits_pharmaceutiques',
        ),
    ]
