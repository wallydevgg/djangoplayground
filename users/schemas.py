from drf_yasg import openapi


class UserSchema:
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
            type=openapi.TYPE_STRING,
            description="Filtrar por esta 1(activo) o 0(inactivo)",
            default=1,
        )
        query = openapi.Parameter(
            "q",
            openapi.IN_QUERY,
            type=openapi.TYPE_STRING,
            description="Filtrar la palabra en los campos username | first_name | last_name",
        )
        return [page, per_page, status, query]

    def updateProfile(self):
        username = openapi.Parameter(
            "username",
            openapi.IN_FORM,
            type=openapi.TYPE_STRING,
            required=True,
        )
        email = openapi.Parameter(
            "email",
            openapi.IN_FORM,
            type=openapi.TYPE_STRING,
            required=True,
        )
        first_name = openapi.Parameter(
            "first_name",
            openapi.IN_FORM,
            type=openapi.TYPE_STRING,
            required=True,
        )
        last_name = openapi.Parameter(
            "last_name",
            openapi.IN_FORM,
            type=openapi.TYPE_STRING,
            required=True,
        )
        avatar = openapi.Parameter(
            "avatar",
            openapi.IN_FORM,
            type=openapi.TYPE_FILE,
            required=False,
        )
        return [
            username,
            email,
            first_name,
            last_name,
            avatar,
        ]
