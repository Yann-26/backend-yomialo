# Generated by Django 5.0 on 2024-07-14 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_id', models.CharField(max_length=100, unique=True)),
                ('site_id', models.CharField(max_length=100)),
                ('trans_date', models.DateTimeField()),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('currency', models.CharField(max_length=10)),
                ('signature', models.CharField(max_length=256)),
                ('payment_method', models.CharField(blank=True, max_length=100, null=True)),
                ('cel_phone_num', models.CharField(blank=True, max_length=20, null=True)),
                ('phone_prefix', models.CharField(blank=True, max_length=10, null=True)),
                ('language', models.CharField(blank=True, max_length=10, null=True)),
                ('version', models.CharField(blank=True, max_length=10, null=True)),
                ('payment_config', models.CharField(blank=True, max_length=50, null=True)),
                ('page_action', models.CharField(blank=True, max_length=50, null=True)),
                ('custom', models.CharField(blank=True, max_length=256, null=True)),
                ('designation', models.CharField(blank=True, max_length=256, null=True)),
                ('error_message', models.TextField(blank=True, null=True)),
                ('status', models.CharField(choices=[('PENDING', 'Pending'), ('SUCCESS', 'Success'), ('FAILED', 'Failed')], default='PENDING', max_length=10)),
            ],
        ),
    ]
