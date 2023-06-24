from django.shortcuts import render, redirect
from .models import Course, Review

def course_list(request):
    return render(request, 'courses/course_list.html', {"courses": Course.objects.all()})

def course_detail(request, pk):

    context = {
        "course": Course.objects.get(id=pk),
        "reviews": Review.objects.filter(course=pk),
    }

    return render(
        request,
        'courses/course_detail.html',
        context
    )


def add_review(request, pk):

    if request.method == "POST":
        course = Course.objects.get(id=pk)
        rating = request.POST.get("rating")
        comment = request.POST.get("comment")
        user = request.user

        Review.objects.create(
            course=course,
            user=user,
            rating=rating,
            comment=comment
        )

    return redirect('course-detail', pk=pk)
from django.test import TestCase
from courses.models import Course, Review, Enrollment
from django.contrib.auth.models import User
from datetime import date


class BaseTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="12345")
        self.course = Course.objects.create(
            title="Python",
            description="Python course",
            start_date=date(2023, 1, 1),
            end_data=date(2023, 1, 10),
            author=self.user,
            price=100.00
        )


class TestCourseModel(BaseTest):

    def test_course_model_str_method(self):
        self.assertEqual(str(self.course), "Python")
class TestReviewModel(BaseTest):

    def setUp(self):
        super().setUp()
        self.review = Review.objects.create(
            user=self.user,
            course=self.course,
            rating=5,
            comment="Great course"
        )

    def test_review_model_str_method(self):
        expected_str = f"{self.user.username} - {self.course.title} - {self.review.rating}"
        self.assertEqual(str(self.review), expected_str)
class TestEnrollmentModel(BaseTest):
    def setUp(self):
        super().setUp()
        self.enrollment = Enrollment.objects.create(
            user=self.user,
            course=self.course
        )

    def test_enrollment_model_str_method(self):
        expected_str = f"{self.user.username} - {self.course.title}"
        self.assertEqual(str(self.enrollment), expected_str)



