from django.urls import path
from . import views

app_name = 'carrinho_app'

urlpatterns = [
    path('adicionar/<int:produto_id>/', views.adicionar_ao_carrinho, name='adicionar_ao_carrinho'),
    path('remover/<int:produto_id>/', views.remover_do_carrinho, name='remover_do_carrinho'),
    path('detalhes/', views.detalhes_carrinho, name='detalhes_carrinho'),
]
