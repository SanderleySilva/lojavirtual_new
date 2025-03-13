from django.shortcuts import get_object_or_404, redirect
from django.views.generic import TemplateView
from .models import Produto, Pedido, Categoria
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


class PagamentoView(LoginRequiredMixin,TemplateView):
    template_name = 'pagamentos/pagamento.html'
    login_url='/usuarios/login/'
    redirect_field_name='redirect_to'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        produto_id = self.kwargs.get('produto_id')
        produto = get_object_or_404(Produto, id=produto_id)
        form = PagamentoForm()
        context['produto'] = produto
        context['form'] = form
        return context

    def post(self, request, *args, **kwargs):
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
    template_name = 'pagamentos/sucesso_pagamento.html'

