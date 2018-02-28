from django.contrib import admin

from .models import BlogPost, Project, Tag


class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'get_tags')


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'link', 'get_tags')


admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Tag)
