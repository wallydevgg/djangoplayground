from rest_framework import generics, parsers, status
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from .serializers import ProductSerializer, ProductCreateSerializer
from .models import Product


class ProductListCreateView(generics.ListCreateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.order_by("id")
    parser_classes = [parsers.MultiPartParser]

    @swagger_auto_schema(request_body=ProductCreateSerializer, operation_summary="gaaa")
    def post(self, _):
        serializer = ProductCreateSerializer(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
