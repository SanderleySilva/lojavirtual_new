# Generated by Django 5.1.6 on 2025-03-12 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carrinho_app', '0002_rename_carro_itemcarrinho_carrinho'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carrinho',
            name='created_at',
        ),
        migrations.AddField(
            model_name='itemcarrinho',
            name='preco',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]
