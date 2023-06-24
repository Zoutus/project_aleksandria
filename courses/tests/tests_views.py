from django.test import TestCase
from courses import factories
from django.urls import reverse


class TestCourseListView(TestCase):

    def setUp(self):
        self.course_1 = factories.CourseFactory()
        self.course_2 = factories.CourseFactory()

    def test_course_list_view(self):
        list_url = reverse("course-list")
        response = self.client.get(list_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "courses/course_list.html")
        self.assertContains(response, self.course_1.title)
        self.assertContains(response, self.course_2.title)




