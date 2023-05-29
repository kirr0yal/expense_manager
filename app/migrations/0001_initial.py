# Generated by Django 4.2 on 2023-04-07 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('modified_at', models.DateField(auto_now=True)),
                ('description', models.CharField(blank=True, max_length=10000, null=True)),
                ('amount', models.IntegerField(default=0)),
            ],
        ),
    ]
