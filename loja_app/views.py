from django.shortcuts import get_object_or_404, redirect
from django.views.generic import TemplateView
from .models import Produto, Pedido, Categoria
from carrinho_app.models import Produto, Carrinho, ItemCarrinho
from .forms import PagamentoForm
from django.contrib.auth.mixins import LoginRequiredMixin



class HomeView(TemplateView):
    template_name = 'estilos/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['produtos'] = Produto.objects.all()
        return context


class ProdutosView(TemplateView):
    template_name = 'produtos/produtos.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categoria'] = Categoria.objects.all()
        return context


class PagamentoView(LoginRequiredMixin, TemplateView):
    template_name = 'pagamentos/pagamento.html'
    login_url = '/usuarios/login/'
    redirect_field_name = 'redirect_to'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        carrinho = get_object_or_404(Carrinho, user=self.request.user)
        itens_carrinho = ItemCarrinho.objects.filter(carrinho=carrinho)
        form = PagamentoForm()
        total_preco = sum(item.total_preco for item in itens_carrinho)
        context['itens_carrinho'] = itens_carrinho
        context['form'] = form
        context['total_preco'] = total_preco
        return context

    def post(self, request, *args, **kwargs):
        carrinho = get_object_or_404(Carrinho, user=self.request.user)
        itens_carrinho = ItemCarrinho.objects.filter(carrinho=carrinho)
        form = PagamentoForm(request.POST)
        if form.is_valid():
            for item in itens_carrinho:
                pedido = form.save(commit=False)
                pedido.produto = item.produto
                pedido.preco_final = item.total_preco
                pedido.save()
                # Adicione a lógica para processar o pagamento (Pix ou Cartão) aqui
            carrinho.delete()  # Limpar o carrinho após o pagamento
            return redirect('loja_app:sucesso_pagamento')
        return self.render_to_response(self.get_context_data(form=form))


def detalhes_produto(request, id):
    produto = get_object_or_404(Produto, id=id)
    return render(request, 'produtos/detalhes_produto.html', {'produto': produto})


class SucessoPagamentoView(TemplateView):
    template_name = 'pagamentos/sucesso_pagamento.html'

