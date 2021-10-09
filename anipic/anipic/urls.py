from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('nouser/', admin.site.urls),
    path('', include('wallpaper.urls')),
    path('', include('quote.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = "アニPIC"
admin.site.site_title = "アニPIC"
admin.site.index_title = "サイト管理"