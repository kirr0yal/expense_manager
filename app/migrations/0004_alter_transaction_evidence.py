# Generated by Django 4.2 on 2023-05-18 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_transaction_evidence'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='evidence',
            field=models.FileField(blank=True, null=True, upload_to='evidence/%Y-%m-%d'),
        ),
    ]
