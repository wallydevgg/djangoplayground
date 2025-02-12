from rest_framework import generics,parsers
from .serializers import tblSupervCanchaSerializer
from .models import tblSupervCancha


class tblSupervCanchaListCreateView(generics.ListCreateAPIView):
    serializer_class = tblSupervCanchaSerializer
    queryset = tblSupervCancha.objects.order_by('intSupervCanchaId')
    parser_classes=[parsers.MultiPartParser]

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
