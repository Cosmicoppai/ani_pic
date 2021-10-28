from django.urls import path
from .views import PicList, NsfwPicList, Home

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('pics/nsfw', NsfwPicList.as_view(), name='nsfw pics', kwargs={'tag':None}),
    path('pics/sfw', PicList.as_view(), name="Sfw pics", kwargs={'tag':None}),
    path('pics/nsfw/<str:tag>', NsfwPicList.as_view(), name='nsfw pics by tag'),
    path('pics/sfw/<str:tag>', PicList.as_view(), name="Sfw pics by tag"),
]