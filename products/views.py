from rest_framework import generics
from .serializers import ProductSerializer
from .models import Product


class ProductListCreateView(generics.ListCreateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.order_by("id")
