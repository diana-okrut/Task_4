from django.contrib.auth.models import User
import pytest
from rest_framework.test import APIRequestFactory

from online_course.course.views import CourseView

from online_course.course.models import Student, Course


@pytest.fixture()
def student_with_no_courses():
    user = User(username="Test")
    user.save()
    student = Student(user=user)
    student.save()
    return student


def test_student_on_course(student_with_no_courses):
    course = Course(name='Test')
    course.save()
    factory = APIRequestFactory()
    request = factory.get(f'/courses/{course.id}')
    view = CourseView.as_view()
    response = view(request)
    print(response)
    assert response.status_code == 200
