from django.contrib import admin

from .models import BlogPost, Project, Tag


admin.site.register(BlogPost)
admin.site.register(Project)
admin.site.register(Tag)
