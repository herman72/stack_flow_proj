from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import logout, authenticate, login

from users.forms import UserRegisterForm, UserLoginForm, UserUpdateForm
from users.models import User


# Create your views here.
def user_register_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'You registered successfully.')
                return redirect('home')
        else:
            messages.warning(request, 'Register unsuccessfully.')

    else:
        form = UserRegisterForm()

    return render(request, 'registration/register.html', {'form': form})


def user_login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful.')
            return redirect('home')
        else:
            messages.warning(request, 'Login unsuccessful.')

    return render(request, 'registration/login.html')


def user_logout_view(request):
    pass


def user_profile_view(request, uid):
    pass


def user_profile_edit_view(request):
    pass


def user_home_view(request):
    return render(request, 'home.html')
