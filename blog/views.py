from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'templates/home.html', {})


def blogs(request):
    return render(request, 'templates/blogs.html', {})


def projects(request):
    return render(request, 'templates/projects.html', {})


def writing(request):
    return render(request, "templates/403.html", {})

def about(request):
    return render(request, "templates/about.html", {})
