from rest_framework import serializers
from .models import WallPaper


class PicSerializer(serializers.ModelSerializer):

    class Meta:
        model = WallPaper
        fields = ['title', 'image']