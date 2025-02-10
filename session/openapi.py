from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from django.urls import path


views = get_schema_view(
    openapi.Info(
        title="DRF Session",
        default_version="1.0",
        description="Documentacion de los endpoints con DRF",
    ),
    permission_classes=[permissions.AllowAny],
    public=True
    
)


urlpatterns = [
    path("swagger-ui", views.with_ui("swagger"), name="swagger-ui"),
    path("redoc/", views.with_ui("redoc"), name="redoc"),
]
 