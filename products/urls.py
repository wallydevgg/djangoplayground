from django.urls import path
from .views import ProductListCreateView, ProductRetrieveCreateUpdateView

urlpatterns = [
    path("", ProductListCreateView.as_view(), name="list_create"),
    path(
        "<int:id>/",
        ProductRetrieveCreateUpdateView.as_view(),
        name="retrieve_delete_destroy",
    ),
]
