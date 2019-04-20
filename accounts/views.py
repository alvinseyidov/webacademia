
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignupForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .models import User, Profile
from courses.models import Course

# login logout & signup

def login_view(request):
    if request.user.is_authenticated:
        return redirect('profile', username=request.user.username)

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('profile', username=user.username)

    form = AuthenticationForm()

    return render(request, 'accounts/login.html', {'form': form})



def logout_view(request):
    logout(request)

    return redirect('home')


def signup(request):
    if request.user.is_authenticated:
        return redirect('profile', username=request.user.username)

    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            # username = form.cleaned_data.get('username')
            # email = form.cleaned_data.get('email')
            # password1 = form.cleaned_data.get('password1')
            # password2 = form.cleaned_data.get('password2')
            user.save()
            Profile.objects.create(user=user)

            raw_username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=raw_username, password=raw_password)
            login(request, user)
            return redirect('profile', username=user.username)


    else:
        form = SignupForm()

    return render(request, 'accounts/signup.html', {'form': form})


# profile

@login_required(login_url='/login/')
def profile(request, username):
    user = get_object_or_404(User, username=username)
    if request.user.username != user.username:
        return redirect('home')

    return render(request, 'accounts/sdashboard.html', {'user': user})



@login_required(login_url='/login/')
def mycourses(request, username):
    user = get_object_or_404(User, username=username)
    if request.user.username != user.username:
        return redirect('home')

    return render(request, 'accounts/smycourses.html', {'user': user})


def cart(request, username):
    user = get_object_or_404(User, username=username)

    return render(request, 'accounts/scart.html', {'user': user})

def addtocart(request, slug):
    user = request.user
    course = get_object_or_404(Course, slug=slug)
    user.profile.cart.add(course)

    return redirect(course.get_absolute_url())




