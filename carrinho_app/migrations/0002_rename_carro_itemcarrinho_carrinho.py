# Generated by Django 5.1.6 on 2025-03-11 20:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carrinho_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='itemcarrinho',
            old_name='carro',
            new_name='carrinho',
        ),
    ]
