from rest_framework import serializers
from django.utils.text import slugify
from session.utils.bucket import Bucket
from .models import Product
from category.serializers import CategorySerializer


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=False)

    class Meta:
        model = Product
        fields = [
            "id",
            "name",
            "description",
            "price",
            "stock",
            "image",
            "category",
            "status",
        ]
        depth = 1


class ProductCreateSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    description = serializers.CharField()
    price = serializers.DecimalField(max_digits=5, decimal_places=2)
    stock = serializers.IntegerField()
    image = serializers.ImageField(write_only=True)
    category_id = serializers.IntegerField()

    def create(self, validated_data):
        image = validated_data.get("image")
        name = validated_data.get("name")
        stream = image.file
        bucket = Bucket("products")
        url = bucket.uploadObject(f"{slugify(name)}.jpg", stream)
        validated_data["image"] = url
        new_record = Product.objects.create(**validated_data)
        new_record.save()
        return new_record
