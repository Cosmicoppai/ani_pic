from rest_framework import status, permissions
from rest_framework.views import APIView
from .models import WallPaper
from .serializers import PicSerializer
from rest_framework.response import Response


class PicList(APIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    @staticmethod
    def get_queryset(_tag):
        if _tag:
            return WallPaper.objects.filter(is_nsfw=False, tag=_tag)
        return WallPaper.objects.filter(is_nsfw=False)

    def get(self, request, **kwargs):
        tag = kwargs['tag']
        wallpapers = self.get_queryset(_tag=tag)
        if wallpapers.exists():
            serializer = PicSerializer(wallpapers, many=True, context={'request': request})
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(headers={"error":"Invalid Tag"},status=status.HTTP_404_NOT_FOUND)


class NsfwPicList(APIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    @staticmethod
    def get_queryset(_tag):
        if _tag:
            return WallPaper.objects.filter(is_nsfw=True, tag=_tag)
        return WallPaper.objects.filter(is_nsfw=True)

    def get(self, request, **kwargs):
        tag = kwargs['tag']
        wallpapers = self.get_queryset(_tag=tag)
        if wallpapers.exists():
            serializer = PicSerializer(wallpapers, many=True, context={'request': request})
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(headers={"error": "Invalid Tag"}, status=status.HTTP_404_NOT_FOUND)
