from django.urls import path
from .views import criar_filmes, pagina_inicial, filme_update, filme_delete, filme_list

urlpatterns = [
    path('', pagina_inicial),
    path('filmes', criar_filmes, name='filme_new'),
    path('filmes/<int:pk>/', filme_update, name='filme_edit'),
    path('filmes/<int:pk>', filme_delete, name='filme_delete'),
    path('filmeteste', filme_list, name='filme_list')
]
