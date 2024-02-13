from django.db import models
from django.contrib.auth.models import User


class InventoryItem(models.Model):
	name = models.CharField(max_length=200)
	stock = models.IntegerField()
	stock_avail = models.IntegerField()
	category = models.ForeignKey('Category', on_delete=models.SET_NULL, blank=True, null=True)
	date_created = models.DateTimeField(auto_now_add=True)
	sku = models.CharField(max_length = 200)
	user = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.name

class Category(models.Model):
	name = models.CharField(max_length=200)

	class Meta:
		verbose_name_plural = 'categories'

	def __str__(self):
		return self.name

class ItemDetails(models.Model):
    inventory_item = models.OneToOneField(InventoryItem, on_delete=models.CASCADE, related_name='details')
    description = models.TextField()
    manufacturer = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    net_stock = models.IntegerField()
	
    def __str__(self):
        return f"{self.inventory_item.name} Details"
	

