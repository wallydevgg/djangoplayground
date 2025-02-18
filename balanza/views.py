from rest_framework import generics, parsers
from .serializers import tblSupervCanchaSerializer, tblPersSeguridadSerializer
from .models import tblSupervCancha, tblPersSeguridad


class tblSupervCanchaListCreateView(generics.ListCreateAPIView):
    serializer_class = tblSupervCanchaSerializer
    queryset = tblSupervCancha.objects.order_by("intSupervCanchaId")
    parser_classes = [parsers.MultiPartParser]

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class tblPersSeguridadListCreateView(generics.ListCreateAPIView):
    serializer_class = tblPersSeguridadSerializer
    queryset = tblPersSeguridad.objects.order_by("intPersSeguridadId")
    parser_classes = [parsers.MultiPartParser]

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
