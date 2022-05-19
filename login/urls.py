from re import template
from django.urls import URLPattern, path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('', auth_views.LoginView.as_view(
        template_name="login/form.html"
    ), name="login"),
    path('logout', auth_views.LogoutView.as_view(), name="logout"),
    path('registrar/', views.UsuariosCreate.as_view(), name="registrar"),
    path('atualiaza/', views.PessoasUpdate.as_view(), name="atualizar-pessoa"),
]