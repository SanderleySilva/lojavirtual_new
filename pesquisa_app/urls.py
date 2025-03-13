from django.urls import path
from . import views

urlpatterns = [
    path('pesquisar/', views.pesquisar, name='pesquisar'),
]