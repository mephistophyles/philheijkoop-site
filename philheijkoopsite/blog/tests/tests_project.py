from django.test import TestCase
from django.urls import resolve, reverse
from django.utils import timezone

from ..models import Project, Tag
from ..views import projects

class ProjectTest(TestCase):
    def setUp(self):
        self.tag = Tag.objects.create(name="testtag")
        self.project = Project.objects.create(title="project test",
                                    description="some test project description",
                                    originally_published_date=timezone.now(),
                                    link="https://google.com",
                                    tags=self.tag)
        url = reverse("projects")
        self.response = self.client.get(url)

    def test_project_list_view_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_project_page_contains_projects(self):
        view = resolve("/projects")
        self.assertEquals(view.func, projects)

    def test_project_page_contains_title(self):
