
from django.shortcuts import render, get_object_or_404
from .models import Course

def courses(request):
    return render(request, 'courses/courses_list.html')


def course_detail(request, slug):
    course = get_object_or_404(Course, slug=slug)

    return render(request, 'courses/course_detail.html', {'course': course})