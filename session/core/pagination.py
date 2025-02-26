from rest_framework import pagination, status
from rest_framework.response import Response


class CustomPagination(pagination.PageNumberPagination):
    page_size_query_param = "per_page"

    def get_paginated_response(self, data):
        return Response(
            {
                "results": data,
                "pagination": {
                    "totalRecords": self.page.paginator.count,
                    "totalPages": self.page.paginator.num_pages,
                    "perPage": self.page.paginator.per_page,
                    "currentPage": self.page.number,
                },
            },
            status=status.HTTP_200_OK,
        )
