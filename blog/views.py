from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return HttpResponse("Hello world")


def index(request):
    return HttpResponse("List of blog posts")


def projects(request):
    return HttpResponse("Project page")


def writing(request):
    return HttpResponse("Writing page")
