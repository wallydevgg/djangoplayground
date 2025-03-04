from rest_framework import generics, status, permissions
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema
from decimal import Decimal
from .serializers import ShoppingCartSerializer, ShoppingCartListSerializer
from .models import ShoppingCart


class ShoppingCartView(generics.ListCreateAPIView):
    serializer_class = ShoppingCartSerializer
    queryset = ShoppingCart.objects
    http_method_names = ["get", "put"]
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = None

    igv = Decimal(0.18)
    prices = {
        "total": 0,
        "subtotal": 0,
        "igv": 0,
    }

    def get_queryset(self):
        queryset = self.queryset.filter(user=self.request.user).all()
        serializer = ShoppingCartListSerializer(queryset, many=True)
        records = serializer.data
        if queryset:
            for item in records:
                price = Decimal(item["price"])
                quantity = item["quantity"]
                self.prices["subtotal"] += price * quantity

            self.prices["igv"] += round(self.prices["subtotal"] * self.igv, 2)
            self.prices["total"] = round(
                self.prices["subtotal"] + self.prices["igv"], 2
            )

        return {"data": records, "prices": self.prices}

    @swagger_auto_schema(
        operation_summary="Endpoint para listar los productos y precios del carrito de compras",
        operation_description="En este servicio podras vizualizar los precios y precio del usuaario conectado",
    )
    def get(self, _):
        record = self.get_queryset()
        return Response(record, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_summary="Endporuint para crear o actulizar un produto en el carrito de compras",
        operation_description="En este servicio se podra crear o actualizar un producto en el carrito de compras del usuario conectado",
    )
    def put(self, request):
        serializer = self.serializer_class(self.request.user, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ShoppingCartDeleteView(generics.DestroyAPIView):
    queryset = ShoppingCartSerializer
    http_method_names = ["delete"]
    permission_classes = [permissions.IsAuthenticated]

    @swagger_auto_schema(
        operation_summary="Endpoint para eliminar un producto del carrito de compras",
        operation_description="En este servicio podras eliminar un producto del carrito de compras",
    )
    # en realidad SOLO borraremos el PRODUCTO del usuasrio que esta logeado
    def delete(self, _, product_id):
        user = self.request.user
        record = get_object_or_404(
            ShoppingCart,
            user_id=user,
            product_id=product_id,
        )
        record.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
