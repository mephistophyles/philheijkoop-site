from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    text = models.TextField()
    originally_published_date = models.DateField(default=timezone.now())
    published_date = models.DateField(blank=True, null=True)

    def publish(self, date=None):
        if date is None:
            date = timezone.now()
        self.published_date = date
        self.save()

    def __str__(self):
        return self.title
