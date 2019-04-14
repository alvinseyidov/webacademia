
from django.urls import path
from . import views

urlpatterns = [
    path('courses/', views.courses, name='courses'),
    path('courses/<str:slug>/', views.course_details, name='course_detail'),
    path('categories/<str:slug>/', views.coursefrom_category, name='coursefrom_category'),
    path('courses/<str:slug>/watch/', views.watch, name='watch'),
    path('courses/<str:courseslug>/watch/<str:videoslug>/', views.watchvideo, name='watchvideo'),
]