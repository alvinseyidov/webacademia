
from django.shortcuts import render, get_object_or_404
from .models import Course, Category
from accounts.models import User


def courses(request):
    courses_list = Course.objects.all()
    categories_list = Category.objects.all()
    return render(request, 'courses/courses_list.html', {'courses': courses_list, 'categories': categories_list})


def course_details(request, slug):
    course = get_object_or_404(Course, slug=slug)
    categories_list = Category.objects.all()
    courses_list = Course.objects.all()


    return render(request, 'courses/course_details.html', {'course': course, 'categories': categories_list, 'courses': courses_list})



def watch(request, slug):
    user = get_object_or_404(User, username=request.user.username)
    course = get_object_or_404(Course, slug=slug)
    videos = Course.video

    return render(request, 'accounts/swatchcourse.html', {'user': user, 'course': course, 'videos': videos})


def categories(request):
    category = Category.objects.all()

    return render(request, 'courses/categories.html', {'categories': category})



def coursefrom_category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    categories_list = Category.objects.all()
    course = Course.objects.all()

    return render(request, 'courses/coursefrom_category.html', {'category': category, 'categories': categories_list, 'courses': course})



