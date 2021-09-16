from django.contrib import admin
from .models import Quote


@admin.register(Quote)
class QuoteAdmin(admin.ModelAdmin):
    ordering = ['created']
    date_hierarchy = 'created'
    search_fields = ('quote', 'tag', 'created')
    list_filter = ('quote', 'tag', 'created')
    list_display = ('quote', 'tag')
