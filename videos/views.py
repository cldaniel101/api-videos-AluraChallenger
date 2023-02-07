# from django.shortcuts import render
from rest_framework import viewsets, filters, generics
from django_filters.rest_framework import DjangoFilterBackend
from .models import *
from .serializer import *

class VideosViewSet(viewsets.ModelViewSet):
    """Exibe todos os videos do banco de dados."""
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['titulo']

class ListaVideosPorCategoria(generics.ListAPIView):
    def get_queryset(self):
        queryset = Video.objects.filter(categoriaId=self.kwargs['pk'])
        return queryset
    serializer_class = ListaVideosPorCategoriaSerializer
