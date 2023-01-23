

from django.urls import path
from .views import detail, signout, signup,signin

urlpatterns = [
    path("", detail, name="home"),
    path("cuentos/", detail, name="cuentos"),
    path("logout/", signout, name="logout"),
    path("signup/", signup, name="signup"),
    path("login/", signin, name="login")
]
