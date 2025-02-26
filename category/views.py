from rest_framework import generics, status, permissions
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from .serializers import CategorySerializer
from .models import Category
from .schemas import CategorySchema

schema = CategorySchema()


class CategoryListCreateView(generics.ListCreateAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.order_by("id")
    permission_classes = [permissions.IsAuthenticated]

    @swagger_auto_schema(
        operation_summary="Endpoint para listar las categorias",
        operation_description="En este endpoint podras listar las categorias",
        manual_parameters=schema.all(),
    )
    def get(self, _):
        query_params = self.request.query_params
        active = query_params.get("status")
        query = query_params.get("q", "")
        filters = {"status": True}

        if active and not int(active):
            filters["status"] = False

        if query:
            filters["name__icontains"] = query

        queryset = self.get_queryset().filter(**filters)
        page = self.paginate_queryset(queryset)
        serializer = self.serializer_class(page, many=True)
        return self.get_paginated_response(serializer.data)

    @swagger_auto_schema(
        operation_summary="Endpoint para crear una categoria",
        operation_description="En este endpoint podras crear una categoria",
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class CategoryRetrieveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects
    lookup_field = "id"
    http_method_names = ["get", "patch", "delete"]
    permission_classes = [permissions.IsAuthenticated]
  
    @swagger_auto_schema(
        operation_summary="Endpoint para traer una categoria por su id",
        operation_description="En este servicio podras traer una categoria por su id",
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Endpoint para actualizar parcialmente una categoria por su id",
        operation_description="En este servicio podras actualizar una categoria por su id",
    )
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Endpoint para inactivar una categoria por su id",
        operation_description="En este servicio podras inactivar una categoria por su id",
    )
    def delete(self, _, id):
        instance = self.get_object()
        instance.status = False
        instance.save()
        response = Response(
            status=status.HTTP_204_NO_CONTENT, data={"message": "Categoria inactivada"}
        )
        response["message"] = "Categoria inactivada"
        return response
