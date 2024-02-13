from django.contrib import admin
from .models import InventoryItem, Category, ItemDetails

admin.site.register(ItemDetails)
admin.site.register(Category)
admin.site.register(InventoryItem)


