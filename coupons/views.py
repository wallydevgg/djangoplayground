from rest_framework import generics, status, permissions
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from .serializers import CouponSerializer
from .models import Coupon


class CouponListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = CouponSerializer
    queryset = Coupon.objects.order_by("id")
    permission_classes = [permissions.IsAuthenticated]

    @swagger_auto_schema(
        operation_summary="Endpoint para listar los cupones creados",
        operation_description="En este servicio se podra visualizar los cupnes que han sido creados",
    )
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Endpoint para listar los cupones creados",
        operation_description="En este servicio se podra visualizar los cupnes que han sido creados",
    )
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class CouponRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CouponSerializer
    queryset = Coupon.objects.order_by("id")
    lookup_field = "id"
    http_method_names = ["get", "patch", "delete"]
    permission_classes = [permissions.IsAuthenticated]

    @swagger_auto_schema(
        operation_summary="Endpoint para listar un cupon por su id",
        operation_description="En este servicio podras listar un cupon por su id",
    )
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Endpoint para actualizar un cupon por su id",
        operation_description="En este servicio se podras actualizar un cupon por su id",
    )
    def patch(self, queryset):
        return super().paginate_queryset(queryset)

    @swagger_auto_schema(
        operation_summary="Endpoint para deshabilitar un cupon por su id",
        operation_description="En este servicio se podra deshabilitar un cupon por su id",
    )
    def delete(self, _, id):
        record = self.get_object()
        record.status = False
        record.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
