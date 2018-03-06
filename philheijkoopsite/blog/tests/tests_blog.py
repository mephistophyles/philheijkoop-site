from django.test import TestCase
from django.urls import resolve, reverse
from django.utils import timezone

from ..models import BlogPost
from ..views import home, BlogPostDetailView, BlogPostListView


class BlogTests(TestCase):
    def setUp(self):
        self.post = BlogPost.objects.create(title='test_title',
                                        text='test_text',
                                        originally_published_date=timezone.now())
        url = reverse('home')
        self.response = self.client.get(url)

    def test_blog_list_view_status_code(self):
        self.assertEquals(self.response.status_code, 200)

    def test_home_url_resolves_home_view(self):
        view = resolve('/')
        self.assertEquals(view.func, home)
