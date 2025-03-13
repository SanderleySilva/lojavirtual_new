from django.db import models

class Pesquisa(models.Model):
    termo = models.CharField(max_length=100)
    data_hora = models.DateTimeField(auto_now_add=True)
