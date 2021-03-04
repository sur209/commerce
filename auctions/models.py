from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
	pass


class Bid(models.Model):
	user = models.CharField(max_length=64, default="", blank=True)
	bid = models.IntegerField()


class Comment(models.Model):
	user = models.CharField(max_length=64, default="", blank=True)
	comment = models.CharField(max_length=256)

	def __str__(self):
		return f"{self.comment}"

class Watchlist(models.Model):
	user = models.CharField(max_length=64, default="", blank=True)
	auctionid = models.IntegerField()


class AuctionList(models.Model):
	user = models.CharField(max_length=64, default="", blank=True)
	auction = models.CharField(max_length=64)
	description = models.CharField(max_length=512, default="")
	img = models.ImageField(default=None, blank=True)
	oferta = models.IntegerField(default=0)
	#monto = models.ManyToManyField(Bid, related_name="Amount", default=0)
	categoria = models.CharField(max_length=64, default="")

	def __str__(self):
		return f"publicación {self.id}: {self.auction} | descripción: {self.description} {self.img} | oferta: {self.oferta} | categoría: {self.categoria}"