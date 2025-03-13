from django.db import models

class Categoria(models.Model):
    """
    Representa uma categoria de produtos.

    Attributes:
        nome (str): Nome da categoria.
        em_oferta (bool): Indica se a categoria está em oferta.
    """
    nome = models.CharField(max_length=20)
    em_oferta = models.BooleanField(default=False)

    def __str__(self):
        """
        Retorna uma representação em string da categoria.

        Returns:
            str: O nome da categoria.
        """
        return self.nome

class Produto(models.Model):
    """
    Representa um produto na loja.

    Attributes:
        nome (str): Nome do produto.
        descricao (str): Descrição do produto.
        preco (int): Preço do produto.
        imagem (ImageField): Imagem do produto.
        categoria (Categoria): A categoria à qual o produto pertence.
    """
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    preco = models.IntegerField()
    imagem = models.ImageField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        """
        Retorna uma representação em string do produto.

        Returns:
            str: O nome do produto.
        """
        return self.nome

class Pedido(models.Model):
    """
    Representa um pedido feito por um cliente.

    Attributes:
        produto (Produto): O produto encomendado.
        nome (str): Nome do cliente.
        endereco (str): Endereço de entrega.
        celular (str): Número de telefone do cliente.
        forma_pagamento (str): Método de pagamento escolhido.
        preco_final (decimal): Preço final do pedido.
    """
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=200)
    celular = models.CharField(max_length=15)
    forma_pagamento = models.CharField(max_length=10, choices=[('pix', 'Pix'), ('cartao', 'Cartão')])
    preco_final = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        """
        Retorna uma representação em string do pedido.

        Returns:
            str: Uma string representando o pedido, incluindo o ID e o nome do produto.
        """
        return f'Pedido #{self.id} - {self.produto.nome}'
