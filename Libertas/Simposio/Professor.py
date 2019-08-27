from django.db import models

class Professor(models.Model):

    nome_prof = models.CharField(max_length = 50)
    telefone = models.CharField(max_length=20)
    email = models.CharField(max_length = 50)
    cpf = models.CharField(max_length = 14)
    usuario = models.CharField(max_length = 20)
    senha = models.CharField(max_length = 20)

    def __str__(self):
        return self.nome_prof