from django.db import models

# Create your models here.

class Post(models.Model):
    autor = models.CharField(max_length =100)
    titulo = models.CharField(max_length =100)
    descricao = models.TextField()
    resumo = models.TextField()

    def __str__(self):
        return self.autor

class Produto(models.Model):
    produto = models.CharField(max_length=100)
    descricao = models.TextField()
    marca = models.TextField()
    preco = models.DecimalField(max_digits=7,decimal_places=2)
    cod_barras = models.CharField(max_length=100)
    fornecedor = models.ForeignKey('Fornecedor', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.produto

class Fornecedor(models.Model):
    nome = models.CharField(max_length=50)
    cnpj = models.CharField(max_length=14)
    endereco = models.CharField(max_length=100)
    cidade= models.ForeignKey('Cidade', on_delete = models.CASCADE, null=True)

    def __str__(self):
        return self.nome

class Cidade(models.Model):
    cinome = models.CharField(max_length=50)
    estado = models.CharField(max_length=50)

    def __str__(self):
        return self.cinome

