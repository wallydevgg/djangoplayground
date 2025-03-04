from rest_framework import serializers
from django.shortcuts import get_object_or_404
from products.models import Product
from .models import ShoppingCart


class ShoppingCartListSerializer(serializers.Serializer):
    id = serializers.IntegerField(source="product.id")
    name = serializers.CharField(source="product.name")
    price = serializers.DecimalField(
        max_digits=10, decimal_places=2, source="product.price"
    )
    quantity = serializers.IntegerField()


class ShoppingCartSerializer(serializers.Serializer):
    product_id = serializers.IntegerField()
    quantity = serializers.IntegerField(min_value=1)

    def update(self, instance, validated_data):
        product_id = validated_data.get("product_id")
        # quantity = validated_data.get("quantity")
        # agregar el id del usuario
        validated_data["user_id"] = instance.id

        get_object_or_404(Product, id=product_id)

        # codigo forma 1: mas descriptiva, misma funcion:
        #        record = ShoppingCart.objects.filter(
        #            user_id=instance, product_id=product_id
        #        ).first()
        #
        #        if record is None:
        #            r ecord = ShoppingCart.objects.create(**validated_data)
        #        else:
        #            record.quantity = quantity
        #
        #        record.save()

        # codigo forma 2: mas compacta, misma funcion:
        ShoppingCart.objects.update_or_create(
            user_id=instance.id, product_id=product_id, defaults=validated_data
        )

        return validated_data
