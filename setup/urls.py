from django.contrib import admin
from django.urls import path, include
from videos.views import *
from categorias.views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register('videos', VideosViewSet, basename='Videos')
router.register('categorias', CategoriasViewSet, basename='Categorias')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('categorias/<int:pk>/videos/', ListaVideosPorCategoria.as_view()),
]
