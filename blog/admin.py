from django.contrib import admin
from .models import BlogPost


class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'slug', 'title', 'timestamp', 'publish_date', 'updated')

    class Meta:
        model = BlogPost


admin.site.register(BlogPost, BlogPostAdmin)