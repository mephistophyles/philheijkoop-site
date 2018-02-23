from django.contrib import admin

from .models import BlogPost, Project, Tag


class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'get_tags')


admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(Project)
admin.site.register(Tag)
