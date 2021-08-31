from rest_framework import status, generics
from .models import WallPaper
from .serializers import PicSerializer


class PicList(generics.ListAPIView):
    serializer_class = PicSerializer

    def get_queryset(self):
        _tag = self.request.query_params.get('tag', None)
        if _tag:
            return WallPaper.objects.filter(tag=_tag, is_nsfw=False)
        return WallPaper.objects.filter(is_nsfw=False)


class NsfwPicList(generics.RetrieveAPIView):
    serializer_class = PicSerializer

    def get_queryset(self):
        _tag = self.request.query_params.get('tag', None)
        if _tag:
            return WallPaper.objects.filter(is_nsfw=True, _tag=_tag)
        return WallPaper.objects.filter(is_nsfw=True)