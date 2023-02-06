from django.contrib import admin
from .models import *

class ListandoVideos(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'descricao', 'url')      #mais qualquer atributo do modelo
    list_display_links = ('id', 'titulo')  #para deixar como link
    search_fields = ('titulo', 'descricao')      #para poder pesquisar no display
    list_per_page = 5                       #para fazer uma paginação

admin.site.register(Video, ListandoVideos)

