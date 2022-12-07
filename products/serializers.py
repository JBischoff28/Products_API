from rest_framework import serializers
from .models import Products

class ProductsSerializer(serializers.ModelSerializer):
    class meta:
        model = Products
        fields = ['title', 'description', 'price', 'inventory_quantity']
