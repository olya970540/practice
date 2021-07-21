from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .forms import UserReg, UserLogin
from django.contrib.auth import login, logout
from django.contrib import messages


def base(request):
    return render(request, 'testt/base.html')

def welcome(request):
    return render(request, 'testt/welcome.html')

def register(request):
    if request.method == 'POST':
        form = UserReg(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Вы зарегистрированы')
            return redirect('login')
        else:
            messages.error(request, 'Ошибка регистрации')
    else:
        form = UserReg()
    return render(request, 'testt/register.html', {"form": form})

def user_login(request):
    if request.method == 'POST':
        form = UserLogin(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('welcome')            
    else:
        form = UserLogin()
    return render(request, 'testt/login.html', {"form": form})

def user_logout(request):
    logout(request)
    return redirect('login')
