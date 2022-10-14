from django.urls import path
from . import views

urlpatterns = [
    path('',views.home),
    path('home/',views.home, name = 'home'),
    path('cadastro/',views.cadastro, name = 'cadastro'),
    path('docad/',views.docad, name = 'validar_cadastro'),
    path('login/',views.login, name = 'login'),
    path('erro/',views.errocad, name = 'erro_cad'),
    path('sucesso/',views.sucessocad, name = 'login_cad'),
]