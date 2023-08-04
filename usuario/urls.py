from django.urls import path
from django.contrib.auth import views as auth_view

from .views import *

urlpatterns = [
path('registro/usuario/', CreateUser.as_view(), name = 'register'),
path('usuario/login/', auth_view.LoginView.as_view(
template_name = 'usuario/register/login.html'
), name = 'login')
]
