from rest_framework import status, permissions
from rest_framework.views import APIView
from .models import Quote
from .serializers import QuoteSerializer
from rest_framework.response import Response


class QuoteList(APIView):
    def __init__(self):
        super().__init__()
        self.permission_classes = [permissions.IsAuthenticatedOrReadOnly]
        self.pagination_class = self.settings.DEFAULT_PAGINATION_CLASS
        self._paginator = self.pagination_class() if self.pagination_class else None

    @staticmethod
    def get_queryset(tag: str):
        if tag:
            return Quote.objects.filter(tag__iexact=tag)
        return Quote.objects.all()

    def get(self, request, **kwargs):
        tag = kwargs['tag']
        quotes = self.get_queryset(tag)
        page = self.paginate_queryset(quotes)
        if page:
            serializer = QuoteSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        return Response(status=status.HTTP_404_NOT_FOUND, headers={"error":"Invalid Tag"})


    def paginate_queryset(self, queryset):
        """
        Return a single page of results, or `None` if pagination is disabled.
        """
        if self._paginator is None:
            return None
        return self._paginator.paginate_queryset(queryset, self.request, view=self)

    def get_paginated_response(self, data):
        """
        Return a paginated style `Response` object for the given output data.
        """
        assert self._paginator is not None
        return self._paginator.get_paginated_response(data)