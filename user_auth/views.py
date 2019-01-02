from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from .form import AuthForm as form

# Create your views here.

def start_page(request):
    return render(request, 'user_auth/start_page.html', {'form': form})

def user_login(request):
    if request.method =='POST':
        username = request.POST['login']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'user_auth/start_page.html', {'form': form})
        else:
            return render(request, 'user_auth/start_page.html', {'form': form, 'msg': 'Логин или пароль - не правильны'})

def user_logout(request):
    logout(request)
    return render(request, 'user_auth/start_page.html', {'form': form})