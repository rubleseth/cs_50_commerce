# Generated by Django 3.0.8 on 2020-08-23 11:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0003_auto_20200823_0751'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listing',
            old_name='starting_price',
            new_name='price',
        ),
    ]
