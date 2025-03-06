from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login as login_django
from django.contrib.auth.models import User


@csrf_exempt
def cadastro(request):
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
            return HttpResponse('As senhas não coincidem.')

        user = User.objects.filter(email=email).first()
        if user:
            return HttpResponse('Já existe um usuário com esse email.')

        username = email.split('@')[0]

        user = User.objects.create_user(username=username, first_name=nome, last_name=sobrenome, email=email, password=senha)
        user.save()
        return HttpResponse(f'O usuário {nome} com o email {email} foi cadastrado com sucesso!')

@csrf_exempt
def login(request):
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


