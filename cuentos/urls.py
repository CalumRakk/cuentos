

from django.urls import path
from .views import detail, signout, signup, signin, results, favorite_update

app_name = 'cuentos'

urlpatterns = [
    path("", results, name="index"),
    path("cuentos/", results, name="index"),

    path("logout/", signout, name="logout"),
    path("signup/", signup, name="signup"),
    path("login/", signin, name="login"),
    path("cuento/<int:cuento_id>", detail, name="detail"),
    path("favorite/<int:cuento_id>", favorite_update, name="favorite")
]
