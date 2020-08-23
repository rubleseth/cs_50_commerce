from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings


class User(AbstractUser):
    pass


class Listing(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,)
    title = models.CharField(max_length=250)
    description = models.TextField()
    image = models.ImageField(upload_to="images")
    price = models.DecimalField(max_digits=1000000, decimal_places=2)

    def __str__(self):
        return f"{self.author} {self.title} {self.price}"


class Bid(models.Model):
    bidder = models.ManyToManyField(settings.AUTH_USER_MODEL)
    bid_item = models.ManyToManyField(Listing)
    bid = models.DecimalField(max_digits=1000000, decimal_places=2)


class Comments(models.Model):
    pass


class Watchlist(models.Model):
    pass
