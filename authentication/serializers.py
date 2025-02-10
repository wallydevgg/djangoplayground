from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework.exceptions import AuthenticationFailed,NotFound
from rest_framework_simplejwt.tokens import RefreshToken
from users.models import User


class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField(min_length=3, max_length=100)
    email = serializers.EmailField(min_length=6, max_length=160)
    password = serializers.CharField(max_length=18, write_only=True)
    password_confirmation = serializers.CharField(max_length=18, write_only=True)

    # validaciones personalizadas
    # https://www.django-rest-framework.org/api-guide/serializers/#validation
    # las validaciones deben estar con un metodo con el prefijo validate_,
    # ejemplo: username -> def validate_username(self,value)

    def validate_password_confirmation(self, value):
        values = self.get_initial()
        if value != values.get("password"):
            raise serializers.ValidationError("Contrasena no coincide")
        return value

    # accion del metodo save()
    def create(self, validated_data):
        # eliminamos el password confirmation de creacion
        validated_data.pop("password_confirmation")
        print(validated_data)
        return User.objects.create_user(**validated_data)


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(min_length=3, max_length=100, write_only=True)
    password = serializers.CharField(max_length=18, write_only=True)
    tokens = serializers.SerializerMethodField()

    # Metodos para el tipo de dato (serializerMethoField)
    # prefijo get_(atributo)
    def get_tokens(self, obj):
        username = obj["username"]
        password = obj["password"]

        user = authenticate(username=username, password=password)
        jwt = RefreshToken.for_user(user)

        return {
            "access_token": str(jwt.access_token),
            "refresh_token": str(jwt),
        }

    def validate(self, attrs):
        username = attrs.get("username")
        password = attrs.get("password")

        # validar que el usuario exista
        # validamos que el hash de la contrasena sea la correcta al ususario
        if not authenticate(username=username, password=password):
            raise AuthenticationFailed(
                "Usuario no existe o las credenciales son invalidas"
            )
        return attrs


class ResetPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()

    def create(self, validated_data):
        return validated_data

    def validate(self, attrs):
        email = attrs.get("email")
        if not User.objects.filter(email=email).exists():
            raise NotFound('No se encontro el usuario, intenta con otro correo')
        return attrs
