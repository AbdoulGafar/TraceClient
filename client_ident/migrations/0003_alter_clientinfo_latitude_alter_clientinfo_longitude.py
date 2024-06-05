# Generated by Django 5.0.6 on 2024-06-03 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client_ident', '0002_alter_clientinfo_fingerprint_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientinfo',
            name='latitude',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True),
        ),
        migrations.AlterField(
            model_name='clientinfo',
            name='longitude',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True),
        ),
    ]
