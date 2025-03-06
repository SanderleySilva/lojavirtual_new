from django import forms
from .models import Pedido

class PagamentoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['nome', 'endereco', 'celular', 'forma_pagamento']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome Completo'}),
            'endereco': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Endereço', 'rows': 3}),
            'celular': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Número de Celular'}),
            'forma_pagamento': forms.Select(attrs={'class': 'form-select'}),
        }
