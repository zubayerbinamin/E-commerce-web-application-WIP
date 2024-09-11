from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Listing(models.Model):
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=64)
    startingbid= models.IntegerField()
    currentprice = models.IntegerField()
    host = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sellingitems")
    bidders = models.ManyToManyField(User, blank=True, related_name="buyingitems")

    def __str__(self):
        return f"{self.id}: {self.title} by {self.host} for {self.currentprice}"
    
class Comments(models.Model):
    body = models.CharField(max_length=64)
    poster = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posters")
    place = models.ForeignKey(User, on_delete=models.CASCADE, related_name="places")
    




