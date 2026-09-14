from django.shortcuts import render, redirect
from .forms import NewUserForm
from .models import Profile
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.contrib.auth import login, logout
from django.shortcuts import get_object_or_404

def register_view(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            age = form.cleaned_data['age']
            about = form.cleaned_data['about']

            us = get_user_model()
            if us.objects.filter(username=username).exists():
                return redirect('login')

            User.objects.create_user(username=username, password=password)
            user = User.objects.get(username=username)
            Profile.objects.create(
                user=user,
                age=age,
                email=email,
                about=about
            )
            login(request, user)
            return redirect('main')
    else:
        form = NewUserForm()

    return render(request, 'accounts/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            us = get_user_model()
            if not us.objects.filter(username=username).exists():
                return redirect('register')
            login(request, form.get_user())
            return redirect('main')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('main')

def delete_view(request):
    if request.method == 'POST':
        request.user.delete()
        return redirect('main')

def account_view(request):
    profile = Profile.objects.get(user=request.user)
    content = {'profile': profile}
    return render(request, 'accounts/account.html', content)
