from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "first_name",
            "last_name",
            "avatar",
            "created_at",
            "updated_at",
        ]


class UserCreateSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    email = serializers.EmailField()
    first_name = serializers.CharField(max_length=150)
    last_name = serializers.CharField(max_length=150)
    password = serializers.CharField(max_length=80, write_only=True)
    # avatar = serializers.ImageField(required=False)

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class UserUpdateSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150, required=False, write_only=True)
    email = serializers.EmailField(required=False, write_only=True)
    first_name = serializers.CharField(max_length=150, required=False, write_only=True)
    last_name = serializers.CharField(max_length=150, required=False, write_only=True)

    message = serializers.ReadOnlyField()

    def update(self, instance, validated_data):
        # instance -> el objeto que recibimos de la instacia del serializador
        # validated_data -> los campos/datos que recibimos del sserializador
        instance.__dict__.update(**validated_data)
        instance.save()
        validated_data["message"] = (
            f"El usuario {instance.username} actualizado correctamente"
        )
        return validated_data
