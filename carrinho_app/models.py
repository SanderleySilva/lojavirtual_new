from django.db import models
from loja_app.models import Produto
from django.contrib.auth.models import User

class Carrinho(models.Model):
    """
    Representa o carrinho de compras de um usuário.

    Attributes:
        user (User): O usuário associado a este carrinho.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class ItemCarrinho(models.Model):
    """
    Representa um item dentro de um carrinho de compras.

    Attributes:
        carrinho (Carrinho): O carrinho ao qual este item pertence.
        produto (Produto): O produto adicionado ao carrinho.
        quantidade (int): A quantidade do produto.
        preco (decimal): O preço do produto.
    """
    carrinho = models.ForeignKey(Carrinho, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField(default=1)
    preco = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)  # Define um valor padrão

    @property
    def total_preco(self):
        """
        Calcula o preço total do item com base na quantidade e no preço unitário.

        Returns:
            decimal: O preço total do item.
        """
        return self.quantidade * self.preco
