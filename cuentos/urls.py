

from django.urls import path
from .views import detail, signout, signup

urlpatterns = [
    path("", detail, name="cuentos"),
    path("logout/", signout, name="logout"),
    path("signup/", signup, name="login")
]
