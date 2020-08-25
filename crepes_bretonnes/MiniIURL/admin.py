from django.contrib import admin
from .models import MiniURL


class MiniURLAdmin(admin.ModelAdmin):
    list_display = ('url', 'mini_url', 'created_at', 'created_by', 'nb_access')
    list_filter = ('created_by',)
    date_hierarchy = 'created_at'
    ordering = ('created_at',)
    search_fields = ('url',)


admin.site.register(MiniURL, MiniURLAdmin)
