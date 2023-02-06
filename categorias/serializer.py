from rest_framework import serializers
from categorias.models import *


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'
        http_method_names = ['get', 'post', 'put', 'patch', 'delete']
    