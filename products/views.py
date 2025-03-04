from rest_framework import generics, parsers, status, permissions
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from django.db.models import Q
from .serializers import (
    ProductSerializer,
    ProductCreateSerializer,
    ProductUpdateSerializer,
)
from .models import Product
from .schemas import ProductSchema

schema = ProductSchema()


class ProductListCreateView(generics.ListCreateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.order_by("id")
    parser_classes = [parsers.MultiPartParser]
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        query_params = self.request.query_params
        active = query_params.get("status")
        query = query_params.get("q", "")
        category_id = query_params.get("category_id")
        filters = {"status": True}

        if active and not int(active):
            filters["status"] = False

        if category_id:
            filters["category_id"] = category_id

        return self.queryset.filter(**filters).filter(
            Q(name__icontains=query) | Q(description__icontains=query)
        )

    @swagger_auto_schema(
        operation_summary="Endpoint para listar productos",
        operation_description="En este servicio podras listar los productos actuales",
        manual_parameters=schema.all(),
    )
    def get(self, request, *args, **kwargs):
        # page = self.paginate_queryset(queryset)
        # serializer = self.serializer_class(page, many=True)
        # return self.get_paginated_response(serializer.data)
        # self.queryset = queryset
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="endpoint para crear un producto",
        operation_description="En este servicio se podra crear un producto",
        request_body=ProductCreateSerializer,
    )
    def post(self, _):
        serializer = ProductCreateSerializer(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ProductRetrieveCreateUpdateView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductUpdateSerializer
    queryset = Product.objects
    lookup_field = "id"
    
    http_method_names = ["get", "patch", "delete"]
    parser_classes = [parsers.MultiPartParser]
    permission_classes = [permissions.IsAuthenticated]

    @swagger_auto_schema(
        operation_summary="endpoint para traer un producto por su id",
        operation_description="en este servicio podras obtener un producto por su id",
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="endpoint para actualizar un producto por su id",
        operation_description="en este servicio podras actualizar un producto por su id",
        request_body=ProductUpdateSerializer,
    )
    def patch(self, _, id):
        record = self.get_object()
        serializer = ProductUpdateSerializer(record, data=self.request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_summary="endpoint para inactivar un productoi por su id",
        operation_description="en este servicio podras inactivar un producto por su id",
    )
    def delete(self, _, id):
        record = self.get_object()
        record.status = False
        record.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
