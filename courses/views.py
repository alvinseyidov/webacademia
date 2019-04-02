
from django.shortcuts import render, get_object_or_404
from .models import Course, Category

def courses(request):
    courses_list = Course.objects.all()

    return render(request, 'courses/courses_list.html', {'courses': courses_list})


def course_detail(request, slug):
    course = get_object_or_404(Course, slug=slug)


    return render(request, 'courses/course_detail.html', {'course': course})



def categories(request):
    category = Category.objects.all()

    return render(request, 'courses/categories.html', {'categories': category})



def coursefrom_category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    course = Course.objects.all()

    return render(request, 'courses/coursefrom_category.html', {'category': category, 'courses': course})