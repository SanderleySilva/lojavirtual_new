from django.urls import path
from . import views



urlpatterns = [
    path('cadastro/', views.cadastro, name= 'cadastro'),
    path('login/', views.login, name= 'login'),
    path('cadastro_sucesso/', views.cadastro_sucesso, name= 'cadastro_sucesso'),
    path('logout/', views.logout_view, name= 'logout'),
]