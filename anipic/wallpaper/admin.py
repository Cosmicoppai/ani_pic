from django.contrib import admin
from .models import WallPaper
from django.contrib.auth.admin import Group


@admin.register(WallPaper)
class AniPicAdmin(admin.ModelAdmin):
    ordering = ['created']
    date_hierarchy = 'created'
    search_fields = ('title', 'tag', 'created')
    list_filter = ('title', 'tag', 'created')


admin.site.unregister(Group)