# Importa funções auxiliares para renderizar templates e redirecionar URLs
from django.shortcuts import render, redirect
# Importa a classe para criar respostas HTTP
from django.http import HttpResponse
# Importa o decorador para desativar a proteção CSRF em views específicas
from django.views.decorators.csrf import csrf_exempt
# Importa funções para autenticação e gerenciamento de login
from django.contrib.auth import authenticate, login as login_django
# Importa o modelo de usuários padrão do Django
from django.contrib.auth.models import User
# Importa a função para logout de usuários
from django.contrib.auth import logout as logout_django

@csrf_exempt
def cadastro(request):
    """
    Exibe o formulário de cadastro e processa a criação de um novo usuário.

    Args:
        request (HttpRequest): O objeto de requisição HTTP.

    Returns:
        HttpResponse: A resposta HTTP com a página de cadastro ou a página de sucesso.
    """
    if request.method == "GET":
        return render(request, 'cadastro.html')
    else:
        nome = request.POST.get('nome')
        sobrenome = request.POST.get('sobrenome')
        email = request.POST.get('email')
        telefone = request.POST.get('telefone')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')

        if senha != confirmar_senha:
            return render(request, 'cadastro.html', {'error_message': 'As senhas não coincidem.'})

        user = User.objects.filter(email=email).first()
        if user:
            return render(request, 'cadastro.html', {'error_message': 'Já existe um usuário com esse email.'})

        username = email.split('@')[0]

        user = User.objects.create_user(username=username, first_name=nome, last_name=sobrenome, email=email, password=senha)
        user.save()
        return render(request, 'cadastro_sucesso.html', {'nome': nome, 'email': email})


@csrf_exempt
def login(request):
    """
    Exibe o formulário de login e processa a autenticação do usuário.

    Args:
        request (HttpRequest): O objeto de requisição HTTP.

    Returns:
        HttpResponse: A resposta HTTP com a página de login ou redirecionamento para a página inicial.
    """
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        user = authenticate(username=email, password=senha)

        if user:
            login_django(request, user)
            return redirect('loja_app:home')
        else:
            return render(request, 'login.html', {'error_message': 'Email ou senha inválidos!'})

def cadastro_sucesso(request):
    """
    Exibe a página de sucesso após o cadastro.

    Args:
        request (HttpRequest): O objeto de requisição HTTP.

    Returns:
        HttpResponse: A resposta HTTP com a página de sucesso do cadastro.
    """
    return render(request, 'cadastro_sucesso.html')

def logout_view(request):
    """
    Faz o logout do usuário e redireciona para a página de login.

    Args:
        request (HttpRequest): O objeto de requisição HTTP.

    Returns:
        HttpResponse: Redireciona para a página de login.
    """
    logout_django(request)
    return redirect('login')
