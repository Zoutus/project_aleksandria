from django.test import TestCase
from django.urls import reverse

from courses import factories


class TestTempleCourseDetail(TestCase):

    def test_template_course_detail_for_logged_in_user(self):
        user = factories.UseFactory()
        course = factories.CourseFactory()
        detail_url = reverse("course")
