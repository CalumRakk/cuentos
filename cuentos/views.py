
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from .models import Cuento

from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError

# Create your views here.


def signup(request: HttpRequest):
    print(request.method)
    form = UserCreationForm
    if request.method == "GET":
        return render(request, "signup.html", {"form": form})

    elif request.method == "POST":
        username = request.POST["username"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]

        if password1 == password2:
            try:
                user = User.objects.create_user(
                    username=username,
                    password=password1)
                user.save()
                login(request, user)
                return redirect("cuentos")
            except IntegrityError:
                return render(request, "signup.html", {"form": form, "msg": "El usuario ya existe"})
        return render(request, "signup.html", {"form": form, "msg": "Las contraseñas no son iguales"})


def signin(request: HttpRequest):
    authentication = AuthenticationForm
    if request.method == "GET":
        return render(request, "login.html", {"form": authentication})

    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect("cuentos")
    return render(request, "login.html", {"form": authentication, "msg": "Datos erroneos"})
    
def signout(request):
    logout(request)
    return redirect("home")


def detail(request, cuento_id):
    print(cuento_id)
    cuento = Cuento.objects.get(pk=cuento_id)   
    cuento.content= cuento.content.split("\n")
    return render(request, "detail.html", {"cuento": cuento})

def index(request):
    cuentos = Cuento.objects.all()
    return render(request, "index.html", {"cuentos": cuentos})
