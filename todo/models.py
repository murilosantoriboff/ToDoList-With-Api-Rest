from django.db import models

class Tarefa(models.Model):
    nome = models.CharField(max_length=100)
    data = models.DateField()
    esta_feita = models.BooleanField()

    def __str__(self) -> str:
        return self.nome
