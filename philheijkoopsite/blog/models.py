from django.db import models
from django.urls import reverse
from django.utils import timezone


class Tag(models.Model):
    name = models.CharField(max_length=255)

    def get_absolute_url(self):
        return reverse('blog:tag_details', kwargs={'slug': self.slug})

    def __str__(self):
        return self.name


class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    originally_published_date = models.DateField(default=timezone.now())
    slug = models.SlugField()
    tags = models.ManyToManyField(Tag)

    class Meta:
        # db_table = 'blog_post'
        ordering = ('originally_published_date',)
        get_latest_by = 'originally_published_date'

    def publish(self, date=None):
        if date is None:
            date = timezone.now()
        self.originally_published_date = date
        self.save()

    def get_tags(self):
        return ",\t".join([str(t) for t in self.tags.all()])

    # def get_absolute_url(self):
    #     return reverse('blog_post:blogpost', kwargs={'slug': self.slug})

    def __unicode__(self):
        return self.title


class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    originally_published_date = models.DateField(default=timezone.now())
    link = models.URLField()
    tags = models.ManyToManyField(Tag)

    class Meta:
        db_table = 'project'

    def publish(self, date=None):
        if date is None:
            date = timezone.now()
        self.originally_published_date = date
        self.save

    def get_tags(self):
        return ",\t".join([str(t) for t in self.tags.all()])

    def __unicode__(self):
        return self.title
