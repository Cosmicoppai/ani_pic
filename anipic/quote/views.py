from rest_framework import status, permissions
from rest_framework.views import APIView
from .models import Quote
from .serializers import QuoteSerializer
from rest_framework.response import Response


class QuoteList(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    @staticmethod
    def get_queryset(tag: str):
        if tag:
            return Quote.objects.filter(tag=tag)
        return Quote.objects.all()

    def get(self, request, **kwargs):
        tag = kwargs['tag']
        quotes = self.get_queryset(tag)
        if quotes.exists():
            serializer = QuoteSerializer(quotes, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND, headers={"error":"Invalid Tag"})