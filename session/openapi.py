from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from django.urls import path


views = get_schema_view(
    openapi.Info(
        title="DRF Playground",
        default_version="2.0",
        description="Documentacion de los endpoints con DRF",
        terms_of_service="https://www.tusitio.com/terms/",
        contact=openapi.Contact(email="wallydevgg@gmail.com"),
        license=openapi.License(name="Apache licencie"),
    ),
    permission_classes=[permissions.AllowAny],
    public=True,
)


urlpatterns = [
    path("swagger-ui", views.with_ui("swagger"), name="swagger-ui"),
    path("redoc/", views.with_ui("redoc"), name="redoc"),
]
