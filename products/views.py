from rest_framework import generics, parsers, status
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from django.db.models import Q
from .serializers import ProductSerializer, ProductCreateSerializer
from .models import Product
from .schemas import ProductSchema

schema = ProductSchema()


class ProductListCreateView(generics.ListCreateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.order_by("id")
    parser_classes = [parsers.MultiPartParser]

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
    pass
