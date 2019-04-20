
from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('users/<str:username>/', views.profile, name='profile'),
    path('users/<str:username>/mycourses/', views.mycourses, name='mycourses'),
    # path('addtocart/courseslug/', views.addtocart, name='addtocart'),
    path('users/<str:username>/cart/', views.cart, name='cart'),
    path('courses/<str:slug>/addtocart/', views.addtocart, name='addtocart'),
]