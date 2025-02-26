from rest_framework import generics, parsers, permissions
from drf_yasg.utils import swagger_auto_schema
from .serializers import tblSupervCanchaSerializer, tblPersSeguridadSerializer
from .models import tblSupervCancha, tblPersSeguridad
from .schemas import BalanzaSchema


schema = BalanzaSchema()


class tblSupervCanchaListCreateView(generics.ListCreateAPIView):
    serializer_class = tblSupervCanchaSerializer
    queryset = tblSupervCancha.objects.order_by("intSupervCanchaId")
    parser_classes = [parsers.MultiPartParser]
    permission_classes = [permissions.IsAuthenticated]

    @swagger_auto_schema(
        operation_summary="endpoint para listar los supervisores de cancha",
        operation_description="En este servicio podras listar los supervisores de cancha",
        manual_parameters=schema.all(),
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="endpoint para crear supervisor de cancha",
        operation_description="En este servicio podras listar supervisores de cancha",
        manual_parameters=schema.all(),
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class tblPersSeguridadListCreateView(generics.ListCreateAPIView):
    serializer_class = tblPersSeguridadSerializer
    queryset = tblPersSeguridad.objects.order_by("intPersSeguridadId")
    parser_classes = [parsers.MultiPartParser]
    permission_classes = [permissions.IsAuthenticated]

    @swagger_auto_schema(
        operation_summary="endpoint para listar personal de seguridad",
        operation_description="En este servicio podras listar personal de seguridad",
        manual_parameters=schema.all(),
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="endpoint para crear personal de seguridad",
        operation_description="En este servicio podras listar personal de seguridad de balanza",
        manual_parameters=schema.all(),
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
