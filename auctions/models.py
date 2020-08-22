from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings


class User(AbstractUser):
    pass


class Listing(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,)
    title = models.CharField(max_length=250)
    description = models.TextField()
    image = models.ImageField


class Bid(models.Model):
    pass


class Comments(models.Model):
    pass


class Watchlist(models.Model):
    pass
