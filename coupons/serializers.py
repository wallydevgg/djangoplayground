from rest_framework import serializers
from .models import Coupon


class CouponSerializer(serializers.ModelSerializer):
    status = serializers.BooleanField(read_only=True)

    class Meta:
        model = Coupon
        fields = ["id", "code", "percentage", "started_at", "ended_at", "status"]
