# 1 crear el serializador
# 2 crear las vistas
# 3 crear las rutas
# CRUD
# create-read(listado|objeto)-update-delete
from django.core.paginator import Paginator
from rest_framework.viewsets import generics
from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer
from .schemas import UserSchema
from .models import User


schema = UserSchema()


# listado | creacion
# /usesrs/
class UserView(generics.GenericAPIView):
    serializer_class = UserSerializer
    # metodos permitidos que hemos definido para la vista en el swagger
    http_method_names = ["get"]

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

        # traer los usaurios que no son del staff -> is_staff
        filters = {"is_staff": False, "is_active": True}
        if active and not int(active):
            filters["is_active"] = False

        records = User.objects.filter(is_staff=False).order_by("id")
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

    def post(self, request):
        pass


# obtener objeto | actualizacion | eliminacion
# /users/{id}
class userGetByIdView(generics.GenericAPIView):
    http_method_names = [""]

    def get(self, request, id):
        pass

    def put(self, request, id):
        pass

    def delete(self, request, id):
        pass
