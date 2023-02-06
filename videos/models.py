from django.db import models
from categorias.models import Categoria

class Video(models.Model):
    categoriaId = models.ForeignKey(to=Categoria, on_delete=models.SET_DEFAULT, default=Categoria.objects.first().pk)
    titulo = models.CharField(max_length=40)
    descricao = models.TextField()
    url = models.URLField(max_length=100, unique=True)
    

    def __str__(self):
        return self.titulo
    