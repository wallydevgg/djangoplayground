from django.urls import path
from .views import CategoryListCreateView, CategoryRetrieveUpdateDelete

urlpatterns = [
    path("", CategoryListCreateView.as_view(), name="list_create"),
    path(
        "<int:id>/",
        CategoryRetrieveUpdateDelete.as_view(),
        name="retrieve_update_delete",
    ),
]
