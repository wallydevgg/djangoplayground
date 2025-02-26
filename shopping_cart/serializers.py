from rest_framework import serializers
from django.shortcuts import get_object_or_404
from products.models import Product
from .models import ShoppingCart


class ShoppingCartSerializer(serializers.Serializer):
    product_id = serializers.IntegerField()
    quantity = serializers.IntegerField(min_value=1)

    def update(self, instance, validated_data):
        product_id = validated_data.get("product_id")
        quantity = validated_data.get("quantity")

        get_object_or_404(Product, id=product_id)
        print(product_id, quantity)
        print(instance)

        return validated_data
