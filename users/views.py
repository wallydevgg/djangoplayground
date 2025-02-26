# 1 crear el serializador
# 2 crear las vistas
# 3 crear las rutas
# CRUD
# create-read(listado|objeto)-update-delete
from django.core.paginator import Paginator
from rest_framework.viewsets import generics
from rest_framework.response import Response
from rest_framework import status, permissions, parsers
from drf_yasg.utils import swagger_auto_schema
from django.db.models import Q
from django.shortcuts import get_object_or_404
from .serializers import (
    UserSerializer,
    UserCreateSerializer,
    UserUpdateSerializer,
    UserProfileSerializer,
)
from .schemas import UserSchema
from .models import User


schema = UserSchema()


# listado | creacion
# /usesrs/
class UserView(generics.GenericAPIView):
    serializer_class = UserSerializer
    http_method_names = ["get", "post"]
    permission_classes = [permissions.IsAuthenticated]

    @swagger_auto_schema(
        operation_summary="Endpoint para listar los usuarios",
        operation_description="Listado de usuarios",
        manual_parameters=schema.all(),
    )
    def get(self, request):  # sourcery skip: merge-dict-assign, move-assign
        # Obtener lo del query params
        query_params = request.query_params
        nro_page = query_params.get("page")
        per_page = query_params.get("per_page")
        active = query_params.get("status")
        query = query_params.get("q", "")
        # traer los usaurios que no son del staff -> is_staff
        filters = {"is_staff": False, "is_active": True}

        if active and not int(active):
            filters["is_active"] = False

        # like es un filtro que se usa para buscar en los campos de texto | en django seria 'contains'
        # ilike es un filtro que se usa para buscar en los campos de texto sin importar si es mayuscula o minuscula | en django seria 'icontains'
        # usaremos 'Q'

        records = (
            User.objects.filter(**filters)
            .filter(
                Q(username__icontains=query)
                | Q(first_name__icontains=query)
                | Q(last_name__icontains=query)
            )
            .order_by("id")
        )

        # offset - limit | 2-8
        pagination = Paginator(records, per_page=per_page)
        page = pagination.get_page(nro_page)
        serializer = self.serializer_class(page.object_list, many=True)
        # datos de paginacion
        # pagination.count=> Total de registros
        # pagination.num_pages=> Total de paginas
        # pagination.per_page=> Total de registros por pagina
        # page.number=>pagina donde nos encontramos
        return Response(
            {
                "results": serializer.data,
                "pagination": {
                    "totalRecords": pagination.count,
                    "totalPages": pagination.num_pages,
                    "perPage": pagination.per_page,
                    "currentPage": page.number,
                },
            },
            status=status.HTTP_200_OK,
        )

    @swagger_auto_schema(
        operation_summary="Endpoint para crear un usuario",
        operation_description="En este servicio podras crear un usuario",
        request_body=UserCreateSerializer,
    )
    def post(self, request):
        serializer = UserCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


# obtener objeto | actualizacion | eliminacion
# /users/{id}
class userGetByIdView(generics.GenericAPIView):
    serializer_class = UserSerializer
    http_method_names = ["get", "put", "delete"]
    permission_classes = [permissions.IsAuthenticated]

    @swagger_auto_schema(
        operation_summary="Endpoint para obtener un usuario",
        operation_description="En este servicio obtenemos los datos del usuario por su id",
    )
    def get(self, _, id):
        # django shortcuts
        record = get_object_or_404(User, pk=id, is_staff=False)
        serializer = self.serializer_class(record)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_summary="Endpoint para actualizar un usuario por su id",
        operation_description="En este servicio actualizamos los datos del usuario por su id",
    )
    def put(self, request, id):
        record = get_object_or_404(User, pk=id, is_staff=False)
        serializer = UserUpdateSerializer(record, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    # soft delete
    @swagger_auto_schema(
        operation_summary="Endpoint para inhabilitar un usuario por su id",
        operation_description="En este servicio podemos desactivar o inhabilitar un usuario por su id",
    )
    def delete(self, request, id):
        record = get_object_or_404(User, pk=id, is_staff=False, is_active=True)
        record.is_active = False
        record.save()
        return Response(
            {"message": f"El usuario {record.username} ha inhabilitado correctamente"},
            status=status.HTTP_200_OK,
        )


class UserProfileView(generics.GenericAPIView):
    serializer_class = UserSerializer
    http_method_names = ["get", "put"]
    permission_classes = [permissions.IsAuthenticated]
    parser_classes = [parsers.MultiPartParser]

    @swagger_auto_schema(
        operation_summary="Endpoint para obtener los datos del usuario conectado",
        operation_description="En este servicio obtenemos el objeto del usuario conectado",
    )
    def get(self, _):
        current_user = self.request.user
        record = get_object_or_404(User, pk=current_user.id)
        serializer = self.serializer_class(record)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_summary="Endpoint para actualizar los datos del usuario conectado",
        operation_description="En este servicio actualizamos los datos del usuario conectado",
        manual_parameters=schema.updateProfile(),
    )
    def put(self, request):
        current_user = self.request.user
        record = get_object_or_404(User, pk=current_user.id)
        serializer = UserProfileSerializer(record, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
