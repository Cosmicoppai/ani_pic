from rest_framework import status, permissions
from rest_framework.generics import GenericAPIView
from .models import WallPaper
from .serializers import PicSerializer
from rest_framework.response import Response
from django.views.generic import TemplateView



class Home(TemplateView):
    template_name = 'index.html'


class PicList(GenericAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    serializer_class = PicSerializer

    def get_queryset(self):
        _tag = self.kwargs['tag']
        if _tag:  # check if tag exists in the url or not
            return WallPaper.objects.filter(is_nsfw=False, tag__iexact=_tag)
        return WallPaper.objects.filter(is_nsfw=False)

    def get(self, request, **kwargs):
        wallpapers = self.get_queryset()
        page = self.paginate_queryset(wallpapers)
        if page:
            serializer = PicSerializer(wallpapers, many=True, context={'request': request})  # pass the context to get the image path with root domain
            return self.get_paginated_response(serializer.data)
        return Response(headers={"error":"Invalid Tag"},status=status.HTTP_404_NOT_FOUND)


class NsfwPicList(GenericAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    serializer_class = PicSerializer

    def get_queryset(self):
        _tag = self.kwargs['tag']
        if _tag:
            return WallPaper.objects.filter(is_nsfw=True, tag__iexact=_tag)
        return WallPaper.objects.filter(is_nsfw=True)

    def get(self, request, **kwargs):
        wallpapers = self.get_queryset()
        page = self.paginate_queryset(wallpapers)
        if page:
            serializer = PicSerializer(wallpapers, many=True, context={'request': request})
            return self.get_paginated_response(serializer.data)
        return Response(headers={"error": "Invalid Tag"}, status=status.HTTP_404_NOT_FOUND)