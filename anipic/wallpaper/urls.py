from django.urls import path
from .views import PicList, NsfwPicList

urlpatterns = [
    path('pics/nsfw/<str:tag>/', NsfwPicList.as_view(), name='nsfw pics'),
    path('pics/<str:tag>/', PicList.as_view(), name="Sfw pics")
]