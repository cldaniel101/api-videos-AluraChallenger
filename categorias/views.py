from rest_framework import viewsets
from .models import *
from .serializer import *


class CategoriasViewSet(viewsets.ModelViewSet):
    """Exibe todas as categorias de videos disponíveis."""
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
