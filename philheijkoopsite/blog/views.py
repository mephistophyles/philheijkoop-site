from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.views.generic import DetailView, ListView

from .models import BlogPost, Tag, Project


class BlogPostListView(ListView):

    model = BlogPost

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['blog_posts'] = BlogPost.objects.all()
        return context


class BlogPostDetailView(DetailView):
    model = BlogPost
    template_name = 'blog/blogpost_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['blog_post'] = BlogPost.objects.get(slug=slug)
        return context


class TagDetailView(DetailView):

    model = Tag

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tag'] = self.tag
        return context


class ProjectListView(ListView):

    model = Project
    template_name = 'projects.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['projects'] = Project.objects.all()
        return context


def home(request):
    return render(request, 'templates/home.html', {})

#
# def blog(request):
#     return render(request, 'templates/blog.html', {'blog_posts': BlogPost.objects.all()})
#
#
# def blogPost(request, slug):
#     try:
#         blog_post = BlogPost.objects.get(slug=slug)
#     except:
#         raise Http404
#     context = super()
#     return render(request, 'templates/blogpost_detail.html', )

def projects(request):
    return render(request, 'templates/projects.html', {})


def writing(request):
    return render(request, "templates/403.html", {})


def about(request):
    return render(request, "templates/about.html", {})
