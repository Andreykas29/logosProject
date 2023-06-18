from django.contrib import admin
from blog.models import Blog


class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'theme', 'date', 'author')
    list_filter = ('theme', 'author', )
    search_fields = ('title', 'theme', )
    list_display_links = ('title', 'theme')


admin.site.register(Blog, BlogAdmin)