from django.shortcuts import render
from  loja_app.models import Produto

def pesquisar(request):
    query = request.GET.get('q')
    if query:
        resultados = Produto.objects.filter(nome__icontains=query)
    return render(request, 'resultados.html', {'query': query, 'resultados': resultados})