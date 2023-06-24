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


to
Everyone


class EnrollmentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "courses.Enrollment"

    user = factory.SubFactory(UserFactory)
    course = factory.SubFactory(CourseFactory)


class ReviewFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "courses.Review"

    user = factory.SubFactory(UserFactory)
    course = factory.SubFactory(CourseFactory)
    rating = factory.Faker("random_int", min=1, max=5)
    comment = factory.Faker("text", max_nb_chars=250)


from django.test import TestCase

from courses import factories


class TestCourseModel(TestCase):

    def setUp(self):
        self.course = factories.CourseFactory(title="Python")

    def test_course_model_str_method(self):
        self.assertEqual(str(self.course), "Python")


class TestReviewModel(TestCase):

    def setUp(self):
        self.review = factories.ReviewFactory()

    def test_review_model_str_method(self):
        expected_str = f"{self.review.user.username} - {self.review.course.title} - {self.review.rating}"
        self.assertEqual(str(self.review), expected_str)


class TestEnrollmentModel(TestCase):
    def setUp(self):
        self.enrollment = factories.EnrollmentFactory()

    def test_enrollment_model_str_method(self):
        expected_str = f"{self.enrollment.user.username} - {self.enrollment.course.title}"
        self.assertEqual(str(self.enrollment), expected_str)