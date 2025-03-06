from rest_framework import serializers
from .models import Order


class OrderSerializer(serializers.Serializer):
    class Meta:
        model = Order
        field = "__all__"


class OrderCreateSerializer(serializers.Serializer):
    shipping_date = serializers.DateTimeField()
