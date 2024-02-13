from rest_framework import serializers
from .models import InventoryItem, Category, ItemDetails

class InventoryItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = InventoryItem
        fields = '__all__'

class ItemDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemDetails
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
