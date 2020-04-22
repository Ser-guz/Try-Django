from django.contrib import admin
from .models import SearchQuery


class SearchQueryAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'query', 'timestamp')

    class Meta:
        model = SearchQuery


admin.site.register(SearchQuery, SearchQueryAdmin)