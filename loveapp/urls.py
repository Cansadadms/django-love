from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name = 'home'),
    path('home/',views.home, name = 'home'),

    path('cadastro/',views.cadastro, name = 'cadastro'),
    path('docad/',views.docad, name = 'validar_cadastro'),
    
    path('login/',views.login, name = 'login'),
    path('dologin/',views.dologin, name = 'logar'),
    path('dologout/',views.dologout, name = 'sair'),

    path('editarperfil/',views.profile, name = 'editar_perfil'),
    path('doupdate/',views.doupdate, name = 'atualizar_perfil'),
    
    path('sucesso/',views.sucessocad, name = 'login_cad'),
    path('errouser/',views.errouser, name = 'erro_cad'),
    path('erromail/',views.erromail, name = 'erro_cad'),
    path('errocnpj/',views.errocnpj, name = 'erro_cad'),

    path('comentario/', views.comentario, name = 'comentario'),
    path('comentario/<int:id>/editar/',views.edit_coment, name='edit_coment'),
]