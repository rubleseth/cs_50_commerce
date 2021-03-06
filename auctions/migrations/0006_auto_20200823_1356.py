# Generated by Django 3.0.8 on 2020-08-23 11:56

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0005_remove_bid_listing_bid'),
    ]

    operations = [
        migrations.AddField(
            model_name='bid',
            name='bid_item',
            field=models.ManyToManyField(to='auctions.Listing'),
        ),
        migrations.AddField(
            model_name='bid',
            name='bidder',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
