from django.db import models

class Diretor(models.Model):
    nome = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Diretores"
        ordering = ["nome"]

    def __str__(self):
        return self.nome


class Categoria(models.Model):
    nome = models.CharField(max_length=50)

    class Meta:
        ordering = ["nome"]

    def __str__(self):
        return self.nome


class Filme(models.Model):
    titulo = models.CharField(max_length=200)
    ano = models.PositiveIntegerField()
    sinopse = models.TextField(blank=True)
    diretor = models.ForeignKey(Diretor, on_delete=models.CASCADE, related_name="filmes")
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name="filmes")

    class Meta:
        ordering = ["titulo"]

    def __str__(self):
        return self.titulo