from rest_framework import serializers
from .models import Category


class CategorySerializer(serializers.ModelSerializer):
    status = serializers.ReadOnlyField()

    class Meta:
        model = Category
        fields = ["id", "name", "status"]
