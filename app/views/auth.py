from django.shortcuts import render, redirect, reverse
from app.models import User
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib import messages

def index(request):
    return render(request, 'app/login.html')

def login_view(request):
    if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
            user_obj = User.objects.filter(username=username)
            user_obj = authenticate(username=username, password=password)
            if user_obj:
                messages.success(request, 'Bạn đã đăng nhập thành công.')
                login(request, user_obj)
                return redirect(reverse('home'))
            else:
                messages.info(request, 'Username hoặc password không đúng')
                return redirect(reverse('login'))

    return render(request, 'app/login.html', {})

def logout_view(request):
    logout(request)
    messages.info(request, "Bạn đã đăng xuất thành công.")
    return redirect(reverse('home'))
