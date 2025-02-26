# from django.shortcuts import render

# Create your views here.

from rest_framework.viewsets import generics
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework_simplejwt.views import TokenViewBase
from rest_framework_simplejwt.serializers import TokenRefreshSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from .serializers import RegisterSerializer, LoginSerializer, ResetPasswordSerializer


# https://www.django-rest-framework.org/api-guide/generic-views/#genericapiview
# permite diferenciar la accion segun el verbo HTTP
# metodos get,post,put,patch,delete
class RegisterView(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    # https://drf-yasg.readthedocs.io/en/stable/custom_spec.html#the-swagger-auto-schema-decorator
    @swagger_auto_schema(
        operation_summary="Endpoint para registrar un usuario",
        operation_description="En este servicio podremos crear un usuario nuevo",
        security=[],
    )
    def post(self, request):
        # intancia al serializador con los datos del body request
        serializer = self.serializer_class(data=request.data)

        # iniciamos la valiacino del serializador
        serializer.is_valid()
        # print(serializer.errors) #visualizar errores

        # ejecutamos la accion (guardado, actualizacion)
        # https://www.django-rest-framework.org/api-guide/serializers/#saving-instances
        serializer.save()

        # para responde al front, usamos el response
        # argumentos de la clase
        # data->la informacion que retornaremos
        # status->codigo de estado HTTP
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    @swagger_auto_schema(
        operation_summary="Endpoint para crear tokens de autenticacion",
        operation_description="en este servicio podemos generar token para acceder a nuestros endpoints",
        security=[],
    )
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status.HTTP_200_OK)


class RefreshView(TokenViewBase):
    serializer_class = TokenRefreshSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    @swagger_auto_schema(
        operation_summary="Endpoint para crear un nuevo token de acceso",
        operation_description="En este servicio podemos generar un nuevo token acceso desde el refresh_token",
    )
    def post(self, request):
        return super().post(request)


class ResetPasswordView(generics.GenericAPIView):
    serializer_class = ResetPasswordSerializer

    @swagger_auto_schema(
        operation_summary="Endpoint para resetear la contrasena",
        operation_description="En este servicio se enviara un correo con la nueva contrasena del usuario",
        security=[],
    )
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
