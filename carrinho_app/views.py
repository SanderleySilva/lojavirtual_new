from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from loja_app.models import Produto
from .models import Carrinho, ItemCarrinho

@login_required(login_url='/usuarios/login/')
def adicionar_ao_carrinho(request, produto_id):
    """
    Adiciona um produto ao carrinho do usuário logado.

    Esta função busca um produto específico pelo seu ID e adiciona esse produto
    ao carrinho do usuário logado. Se o produto já estiver no carrinho, a quantidade
    será incrementada. Caso contrário, um novo item será criado com a quantidade inicial.

    Args:
        request: O objeto de requisição HTTP.
        produto_id (int): O ID do produto a ser adicionado.

    Returns:
        HttpResponse: Redireciona o usuário para a página de detalhes do carrinho.
    """
    produto = get_object_or_404(Produto, id=produto_id)
    carrinho, created = Carrinho.objects.get_or_create(user=request.user)
    item_carrinho, created = ItemCarrinho.objects.get_or_create(carrinho=carrinho, produto=produto)

    if not created:
        item_carrinho.quantidade += 1
    else:
        item_carrinho.preco = produto.preco
    item_carrinho.save()

    return redirect('carrinho_app:detalhes_carrinho')

@login_required(login_url='/usuarios/login/')
def remover_do_carrinho(request, produto_id):
    """
    Remove um produto do carrinho do usuário logado.

    Esta função busca um produto específico pelo seu ID e remove esse produto
    do carrinho do usuário logado.

    Args:
        request: O objeto de requisição HTTP.
        produto_id (int): O ID do produto a ser removido.

    Returns:
        HttpResponse: Redireciona o usuário para a página de detalhes do carrinho.
    """
    produto = get_object_or_404(Produto, id=produto_id)
    carrinho = Carrinho.objects.get(user=request.user)
    item_carrinho = ItemCarrinho.objects.get(carrinho=carrinho, produto=produto)

    item_carrinho.delete()

    return redirect('carrinho_app:detalhes_carrinho')

@login_required(login_url='/usuarios/login/')
def detalhes_carrinho(request):
    try:
        carrinho = Carrinho.objects.get(user=request.user)
        itens_carrinho = ItemCarrinho.objects.filter(carrinho=carrinho)
        total_preco = sum(item.total_preco for item in itens_carrinho)
        return render(request, 'carrinho/detalhes_carrinho.html', {'carrinho': carrinho, 'itens_carrinho': itens_carrinho, 'total_preco': total_preco})
    except Carrinho.DoesNotExist:
        return render(request, 'carrinho/detalhes_carrinho.html', {'itens_carrinho': [], 'total_preco': 0, 'mensagem': "Seu carrinho está vazio."})
