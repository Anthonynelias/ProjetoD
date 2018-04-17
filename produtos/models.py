from django.db import models


class DadosProdutos(models.Model):
    nome = models.CharField(max_length=100, verbose_name='Nome do produto')
    valor = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Valor do produto', default=1)
    quantidade = models.IntegerField(verbose_name='Quantidade estoque')
    imagem = models.ImageField(
        null = True,
        blank = True,
        upload_to = 'iimagens'
    )

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Dados Produtos'
        verbose_name_plural = 'Dados Produtos'
