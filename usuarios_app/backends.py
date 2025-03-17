# usuarios_app/backends.py
"""
Este módulo define um backend de autenticação personalizado para o Django.

Classe:
    EmailBackend (ModelBackend):
        Um backend de autenticação que permite aos usuários fazer login usando o endereço de e-mail em vez do nome de usuário padrão.

Métodos:
    authenticate(self, request, username=None, password=None, **kwargs):
        Autentica um usuário com base no e-mail (em vez do nome de usuário padrão) e na senha.

Uso:
    Substitui o backend padrão de autenticação do Django para implementar a funcionalidade de login via e-mail.
    Deve ser configurado nas configurações do Django como backend de autenticação.
"""

from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

class EmailBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        UserModel = get_user_model()
        try:
            user = UserModel.objects.get(email=username)
        except UserModel.DoesNotExist:
            return None
        else:
            if user.check_password(password):
                return user
        return None
