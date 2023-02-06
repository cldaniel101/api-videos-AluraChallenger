from django.db import models

class Categoria(models.Model):
    CORES = (
        ('VM', 'Vermelho'),
        ('VD', 'Verde'),
        ('AZ', 'Azul'),
        ('AM', 'Amarelo'),
        ('L', 'Laranja'),
        ('R', 'Rosa'),
    )
    titulo = models.CharField(max_length=40)
    cor = models.CharField(max_length=2, choices=CORES, blank=False, null=False, default='VM')

    def __str__(self):
        return self.titulo
