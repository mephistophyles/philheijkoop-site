from django.db import models
from django.utils import timezone


class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    originally_published_date = models.DateField(default=timezone.now())
    slug = models.SlugField()
    tags = models.ManyToManyField(Tag)

    def publish(self, date=None):
        if date is None:
            date = timezone.now()
        self.originally_published_date = date
        self.save()

    def __str__(self):
        return self.title


class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    originally_published_date = models.DateField(default=timezone.now())
    link = models.URLField()
    tags = models.ManyToManyField(Tag)

    def publish(self, date=None):
        if date is None:
            date = timezone.now()
        self.originally_published_date = date
        self.save

    def __str__(self):
        return self.title
