from django.urls import path
from .views import *

app_name= 'loja_app'

urlpatterns = [
    path('', HomeView.as_view(), name= 'home'),
    path('produtos/', ProdutosView.as_view(), name= 'produtos'),
    path('pagamento/<int:produto_id>/', PagamentoView.as_view(), name='pagamento'),
    path('sucesso_pagamento/', SucessoPagamentoView.as_view(), name='sucesso_pagamento'),
]