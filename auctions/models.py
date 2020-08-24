from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings


class User(AbstractUser):
    pass


class Listing(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=100000000, decimal_places=2)
    created_date = models.DateTimeField("Date Created")


class Bid(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    bid = models.DecimalField(max_digits=100000000, decimal_places=2, null=True)
    bid_item = models.ForeignKey("Listing", on_delete=models.CASCADE, null=True)
