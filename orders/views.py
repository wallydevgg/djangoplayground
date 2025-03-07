from rest_framework import generics, status, permissions, exceptions
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from django.db import transaction
from .serializers import OrderSerializer, OrderCreateSerializer
from products.models import Product
from shopping_cart.models import ShoppingCart
from .models import Order, OrderItem
from decimal import Decimal


class OrderListCreateView(generics.ListCreateAPIView):
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]
    http_method_names = ["post"]

    @swagger_auto_schema(
        operation_summary="Endpoint para crear un pedido/orden",
        operation_description="En este servicio se puede crear un pedido/orden",
        request_body=OrderCreateSerializer,
    )
    def post(self, _):
        request = self.request.data
        current_user = self.request.user
        shippping_date = request.get("shipping_date")

        with transaction.atomic():
            # validar los productos en el carrito sde compras  y retornar los precios y productos del carrito
            prices, shopping_cart = self.__validateShoppingCart(current_user)

            # crear la orden/pedido
            order = Order.objects.create(
                user=current_user,
                total_price=prices["total"],
                subtotal_price=prices["subtotal"],
                igv_price=prices["igv"],
                shipping_date=shippping_date,
            )
            order.save()

            # agregamos los items del pedido
            items = [
                OrderItem(
                    order_id=order.id,
                    product_id=value.product.id,
                    price=value.product.price,
                    quantity=value.quantity,
                )
                for value in shopping_cart
            ]

            OrderItem.objects.bulk_create(items)

            # crear el url de pago - *Pendiente

            # Reducir el stock de los productos

            reduces = self.__reduceStockProducts(shopping_cart)
            Product.objects.bulk_update(reduces, ["stock"])

            # eliminamos el carrito de compras
            ShoppingCart.objects.filter(user=current_user).delete()

        return Response(status=status.HTTP_200_OK)

    def __validateShoppingCart(self, current_user):
        prices = {"subtotal": 0}
        igv = Decimal(0.18)
        shopping_cart = ShoppingCart.objects.filter(user=current_user).all()

        if not shopping_cart:
            raise exceptions.NotFound("Shopping cart is empity!")

        for item in shopping_cart:
            price = item.product.price
            quantity = item.quantity
            prices["subtotal"] += price * quantity

        prices["igv"] = round(prices["subtotal"] * igv, 2)

        prices["total"] = round(prices["subtotal"] + prices["igv"], 2)

        return prices, shopping_cart

    def __reduceStockProducts(self, items):
        updates = []

        for item in items:
            record = Product.objects.filter(id=item.product.id).first()
            new_stock = record.stock - item.quantity
            record.__dict__.update(stock=new_stock)
            updates.append(record)

        return updates
