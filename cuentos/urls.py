

from django.urls import path
from .views import detail, signout, signup,signin,index


urlpatterns = [
    path("", index, name="home"),
    path("cuentos/", index, name="cuentos"),
    path("logout/", signout, name="logout"),
    path("signup/", signup, name="signup"),
    path("login/", signin, name="login"),
    path("cuentos/<int:cuento_id>", detail, name="login")
]
