from rest_framework import generics, status, permissions
from rest_framework.response import Response
from .serializers import ShoppingCartSerializer
from .models import ShoppingCart


class ShoppingCartView(generics.ListCreateAPIView):
    serializer_class = ShoppingCartSerializer
    queryset = ShoppingCart.objects
    http_method_names = ["put"]
    permission_classes = [permissions.IsAuthenticated]

    def put(self, request):
        serializer = self.serializer_class(self.request.user, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_200_OK)
