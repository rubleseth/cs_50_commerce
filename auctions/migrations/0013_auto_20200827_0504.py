# Generated by Django 3.0.8 on 2020-08-27 03:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0012_watchlist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='created_date',
            field=models.DateTimeField(auto_now=True, verbose_name='Date Created'),
        ),
    ]
