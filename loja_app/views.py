from django.shortcuts import get_object_or_404, redirect
from django.views.generic import TemplateView
from .models import Produto, Pedido, Categoria
from .forms import PagamentoForm
from django.contrib.auth.mixins import LoginRequiredMixin


class HomeView(TemplateView):
    """
    Visão para a página inicial da loja.

    Attributes:
        template_name (str): Caminho para o template da página inicial.
    """

    template_name = 'estilos/home.html'

    def get_context_data(self, **kwargs):
        """
        Adiciona produtos ao contexto da página inicial.

        Args:
            **kwargs: Outros argumentos de contexto.

        Returns:
            dict: O contexto atualizado contendo os produtos.
        """
        context = super().get_context_data(**kwargs)
        context['produtos'] = Produto.objects.all()
        return context


class ProdutosView(TemplateView):
    """
    Visão para a página de produtos.

    Attributes:
        template_name (str): Caminho para o template da página de produtos.
    """

    template_name = 'produtos/produtos.html'

    def get_context_data(self, **kwargs):
        """
        Adiciona categorias ao contexto da página de produtos.

        Args:
            **kwargs: Outros argumentos de contexto.

        Returns:
            dict: O contexto atualizado contendo as categorias.
        """
        context = super().get_context_data(**kwargs)
        context['categoria'] = Categoria.objects.all()
        return context


class PagamentoView(LoginRequiredMixin, TemplateView):
    """
    Visão para a página de pagamento, protegida por autenticação.

    Attributes:
        template_name (str): Caminho para o template da página de pagamento.
        login_url (str): URL para a página de login.
        redirect_field_name (str): Nome do campo de redirecionamento após login.
    """

    template_name = 'pagamentos/pagamento.html'
    login_url = '/usuarios/login/'
    redirect_field_name = 'redirect_to'

    def get_context_data(self, **kwargs):
        """
        Adiciona produto e formulário de pagamento ao contexto.

        Args:
            **kwargs: Outros argumentos de contexto.

        Returns:
            dict: O contexto atualizado contendo o produto e o formulário de pagamento.
        """
        context = super().get_context_data(**kwargs)
        produto_id = self.kwargs.get('produto_id')
        produto = get_object_or_404(Produto, id=produto_id)
        form = PagamentoForm()
        context['produto'] = produto
        context['form'] = form
        return context

    def post(self, request, *args, **kwargs):
        """
        Processa a submissão do formulário de pagamento.

        Args:
            request (HttpRequest): O objeto de requisição HTTP.
            *args: Argumentos adicionais.
            **kwargs: Outros argumentos de contexto.

        Returns:
            HttpResponse: Redireciona para a página de sucesso de pagamento se o formulário for válido,
            caso contrário, renderiza a página de pagamento novamente com os erros do formulário.
        """
        produto_id = self.kwargs.get('produto_id')
        produto = get_object_or_404(Produto, id=produto_id)
        form = PagamentoForm(request.POST)
        if form.is_valid():
            pedido = form.save(commit=False)
            pedido.produto = produto
            pedido.save()
            # Adicione a lógica para processar o pagamento (Pix ou Cartão) aqui
            return redirect('loja_app:sucesso_pagamento')
        return self.render_to_response(self.get_context_data(form=form, produto=produto))


class SucessoPagamentoView(TemplateView):
    """
    Visão para a página de sucesso do pagamento.

    Attributes:
        template_name (str): Caminho para o template da página de sucesso do pagamento.
    """

    template_name = 'pagamentos/sucesso_pagamento.html'
