from django.db import models
from app.custom_models import SeparatedValuesField

# voucher model
class Voucher(models.Model):
    title = models.CharField(max_length=15)
    description = models.TextField() 
    capacity = models.IntegerField()                                                                 
    vouchtype = models.TextField()
    vouchvalue = models.TextField()

# product
class Product(models.Model):
	title = models.CharField(max_length=10)
	price = models.FloatField()

# client
class CltCart(models.Model):
	client_tag = models.CharField(max_length=15)
	client_item = models.TextField()
	client_payable = models.FloatField()
	client_fee = models.FloatField()

