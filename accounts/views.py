
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .models import User

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
    return render(request, 'accounts/signup.html')


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


































