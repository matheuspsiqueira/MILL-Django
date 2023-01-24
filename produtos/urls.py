from django.urls import path
from .views import *

urlpatterns = [
    path('estoque', estoque, name='estoque'),
    path('cadastra/produto', cadastra_produto, name='cadastra_produto'),
    path('deleta/<int:produto_id>', deleta_produto, name='deleta_produto'),
    path('edita/<int:produto_id>', edita_produto, name='edita_produto'),
    path('atualiza_produto', atualiza_produto, name='atualiza_produto')
]