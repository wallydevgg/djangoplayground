from drf_yasg import openapi


class ProductSchema:
    def all(self):
        page = openapi.Parameter(
            "page", openapi.IN_QUERY, type=openapi.TYPE_INTEGER, default=1
        )
        per_page = openapi.Parameter(
            "per_page", openapi.IN_QUERY, type=openapi.TYPE_INTEGER, default=10
        )
        status = openapi.Parameter(
            "status",
            openapi.IN_QUERY,
            type=openapi.TYPE_INTEGER,
            description="Filtrar por estado 1 (activo) o 0 (inactivo)",
            default=1,
        )
        query = openapi.Parameter(
            "q",
            openapi.IN_QUERY,
            type=openapi.TYPE_STRING,
            description="Filtrar la palabra en los campos name | description",
        )
        category_id = openapi.Parameter(
            "category_id",
            openapi.IN_QUERY,
            type=openapi.TYPE_INTEGER,
        )
        return [page, per_page, query, category_id, status]
