from django.db import models
from user.models import User

# Create your models here.
class Shop_Apply(models.Model):

	owner = models.ForeignKey(User)
	shop_name = models.CharField(max_length=50)
	address = models.CharField(max_length=100)
	regi_num = models.CharField(max_length=30, blank=True, unique=True)
	category = models.CharField(max_length=20)
	applied = models.DateTimeField()
	approved = models.DateTimeField(null=True)

	def is_approved(self):

		return bool(self.approved)


class Shop(models.Model):

	owner = models.ForeignKey(User)
	apply_id = models.ForeignKey(Shop_Apply)
	longitude = models.DecimalField(max_digits=9, decimal_places=6)
	latitude = models.DecimalField(max_digits=9, decimal_places=6)
	description = models.TextField(blank=True)
	shop_phone1 = models.CharField(max_length=13, blank=True)
	shop_phone2 = models.CharField(max_length=13, blank=True)
	is_available = models.BooleanField(default=1)
	img = models.CharField(max_length=255, blank=True, null=True)
	thumbnail = models.CharField(max_length=255, blank=True, null=True)
	open = models.SmallIntegerField()
	close = models.SmallIntegerField()



class Menu(models.Model):
	menu_name = models.CharField(max_length=50)
	shop = models.ForeignKey(Shop)
	price = models.IntegerField(10)	
	description = models.CharField(max_length=200, blank=True)
	img = models.CharField(max_length=200, blank=True)
	is_serving = models.BooleanField()

	def is_serving(self):
		return bool(self.serving)

	class Meta:
		unique_together = ('menu_name', 'shop', )
	
