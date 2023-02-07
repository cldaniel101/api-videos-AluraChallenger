from rest_framework import serializers
from videos.models import *
from .validators import *

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'

    def validate(self, data):
        if not valida_url(data['url']):
            raise serializers.ValidationError({'url': 'Esta não é uma url de vídeo válida.'})
        return data

class ListaVideosPorCategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        exclude = ['categoriaId']   