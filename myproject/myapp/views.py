from django.shortcuts import render, redirect

from django.contrib.auth.models import auth, User
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.


def index(req):
    context = {
        'title': 'Главная'
    }
    return render(req, 'myapp/index.html', context)


def load(req):
    return render(req, 'myapp/load.html')


def inference(req):
    return render(req, 'myapp/inference.html')


def login(req):
    context = {}

    if req.method == 'POST':
        username = req.POST.get('username')
        password = req.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(req, user)
            return redirect('load')
        else:
            messages.info(req, 'user not found or password is incorrect')
            return redirect('login')
    else:
        return render(req, 'myapp/login.html', context)


def register(req):
    context = {}

    if req.method == "POST":
        username = req.POST.get('username')
        password1 = req.POST.get('password1')
        password2 = req.POST.get('password2')
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(req, 'username already exists')
                print('Пользователь с таким именем уже существует')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password1)
                user.save()
                print('registred ' + username)
                return redirect('login')
        else:
            messages.info(req, 'passwords are different')
            print('Пароли различаются')
            return redirect('register')
    else:
        return render(req, 'myapp/register.html', context)


def logout(req):
    auth.logout(req)
    return render(req, 'myapp/index.html')

def news(req):
    return render(req, 'myapp/news.html')