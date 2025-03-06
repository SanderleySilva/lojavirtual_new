from django.db import models



class Categoria(models.Model):
    nome= models.CharField(max_length=20)
    em_oferta = models.BooleanField(default=False)

    def __str__(self):
        return self.nome


class Produto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    preco = models.IntegerField()
    imagem = models.ImageField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome
    



    


class Pedido(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=200)
    celular = models.CharField(max_length=15)
    forma_pagamento = models.CharField(max_length=10, choices=[('pix', 'Pix'), ('cartao', 'Cartão')])
    preco_final = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f'Pedido #{self.id} - {self.produto.nome}'
