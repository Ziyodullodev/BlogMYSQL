from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login, logout

from .models import *
# Create your views here.
from django.contrib.auth.models import User

class Register(View):
    def get(self, request):
        return render(request, 'register.html')
    def post(self, request):
        a = User.objects.create_user(
            username=request.POST['login'],
            password=request.POST['parol'],
        )
        login(request, a)
        return redirect('/')

class Login(View):
    def get(self, request):
        return render(request, 'login.html')
    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is None:
            return redirect('login')
        else:
            login(request, user)
            return redirect('/')

def Logout(request):
    logout(request)
    return redirect('/login')

class Home(View):
    def get(self, request):
        if request.user.is_authenticated:
            hamma = Maqola.objects.all()
            return render(request, 'Home.html', {'maqolalar': hamma})
        else:
            return redirect('/login')

class Maqolalar(View):
    def get(self, request, son):
        if request.user.is_authenticated:
            maqola = Maqola.objects.get(id=son)
            return render(request, 'maqola.html', {'M': maqola})
        else:
            return redirect('/login')


class AddMaqola(View):
    def get(self, request):
        if request.user.is_authenticated:
            muallif = User.objects.all()
            return render(request, 'Maqola_qoshish.html', {'M': muallif})
        else:
            return redirect('/login')
    def post(self, request):
        m = request.POST['muallif']
        muallif1 = User.objects.get(id=m)
        Maqola.objects.create(
            sarlavha=request.POST['sarlavha'],
            mavzu=request.POST['sarlavha'],
            matn=request.POST['sarlavha'],
            muallif = muallif1
        )
        return redirect('/')