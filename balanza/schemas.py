from drf_yasg import openapi


class BalanzaSchema:
    def all(self):
        page = openapi.Parameter(
            "page", openapi.IN_QUERY, type=openapi.TYPE_INTEGER, default=1
        )
        per_page = openapi.Parameter(
            "per_page", openapi.IN_QUERY, type=openapi.TYPE_INTEGER, default=10
        )
        query = openapi.Parameter(
            "q",
            openapi.IN_QUERY,
            type=openapi.TYPE_STRING,
            description="Filtrar la palabra en los campos name | description",
        )

        return [page, per_page, query]
