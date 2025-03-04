from django.urls import path
from .views import ShoppingCartView, ShoppingCartDeleteView

urlpatterns = [
    path("", ShoppingCartView.as_view(), name="list_create"),
    path("<int:product_id>/", ShoppingCartDeleteView.as_view(), name="delete"),
]
