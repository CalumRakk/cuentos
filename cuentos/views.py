
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest, JsonResponse
from .models import Cuento, Favorite

from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.core.exceptions import ObjectDoesNotExist


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
                return redirect("/")
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
    print(user)
    if user is not None:
        login(request, user)
        return redirect("/")

    return render(request, "login.html", {"form": authentication, "msg": "Datos erroneos"})


def signout(request):
    logout(request)
    return redirect("/")


def detail(request: HttpRequest, cuento_id):
    cuento = Cuento.objects.get(pk=cuento_id)
    cuento.content = cuento.content.replace("-", "─ ")
    cuento.content = cuento.content.split("\n")
    is_favorite = False
    user = request.user
    if user is not None:
        try:
            is_favorite = bool(Favorite.objects.get(
                cuento=cuento.id, user=user.id))
        except ObjectDoesNotExist:
            is_favorite = False

    return render(request, "detail.html", {"cuento": cuento, "is_favorite": is_favorite})


def favorite_update(request: HttpRequest, cuento_id):
    user= request.user
    is_favorite= False
    is_login= user.is_authenticated      
    if request.method=="POST":
        cuento = Cuento.objects.get(pk=cuento_id)
        if is_login:
            favorite, created = Favorite.objects.get_or_create(
                cuento=cuento, user=user)         
            if created is True:           
                favorite.save()
                is_favorite = True
            else:
                favorite.delete()
                is_favorite = False 

    data = {"is_favorite": is_favorite, "is_login": is_login}
    return JsonResponse(data)


def results(request):
    cuentos = Cuento.objects.all()
    return render(request, "cuentos.html", {"cuentos": cuentos})
    
def index(request):
    cuentos = Cuento.objects.all()
    return render(request, "index.html", {"cuentos": cuentos})


def favorite(request, object_id):
    print(request.POST)
