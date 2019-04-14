
from django.shortcuts import render, get_object_or_404
from .models import Course, Category, Videos
from accounts.models import User
from django.contrib.auth.decorators import login_required

# courses

def courses(request):
    courses_list = Course.objects.all()
    categories_list = Category.objects.all()
    return render(request, 'courses/courses_list.html', {'courses': courses_list, 'categories': categories_list})


def course_details(request, slug):
    course = get_object_or_404(Course, slug=slug)
    categories_list = Category.objects.all()
    courses_list = Course.objects.all()


    return render(request, 'courses/course_details.html', {'course': course, 'categories': categories_list, 'courses': courses_list})


def coursefrom_category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    categories_list = Category.objects.all()
    course = Course.objects.all()

    return render(request, 'courses/coursefrom_category.html', {'category': category, 'categories': categories_list, 'courses': course})



# watch courses

@login_required(login_url='/login/')
def watch(request, slug):
    user = get_object_or_404(User, username=request.user.username)
    course = get_object_or_404(Course, slug=slug)
    videos = Course.video

    return render(request, 'accounts/swatchcourse.html', {'user': user, 'course': course, 'videos': videos})

@login_required(login_url='/login/')
def watchvideo(request, courseslug, videoslug):
    user = get_object_or_404(User, username=request.user.username)
    course = get_object_or_404(Course, slug=courseslug)
    videos = Course.video
    video = get_object_or_404(Videos, videoslug=videoslug)

    return render(request, 'accounts/swatchcourse.html', {'user': user, 'course': course, 'videos': videos, 'video': video})







