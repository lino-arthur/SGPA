
from django.contrib import admin
from django.urls import path

from animais.views import (
    dashboard,
    lista_animais,
    novo_animal,
    detalhes_animal,
    editar_animal,
    excluir_animal,
)

from historico_veterinario.views import (
    lista_historicos,
    novo_historico,
    detalhes_historico,
    editar_historico,
    excluir_historico,
)

from adocoes.views import (
    lista_adocoes,
    nova_adocao,
    detalhes_adocao,
    editar_adocao,
    excluir_adocao,
)


urlpatterns = [
    path("admin/", admin.site.urls),

    # Dashboard
    path("", dashboard, name="dashboard"),

    # Animais
    path("animais/", lista_animais, name="lista_animais"),
    path("animais/novo/", novo_animal, name="novo_animal"),
    path("animais/<int:animal_id>/", detalhes_animal, name="detalhes_animal"),
    path("animais/<int:animal_id>/editar/", editar_animal, name="editar_animal"),
    path("animais/<int:animal_id>/excluir/", excluir_animal, name="excluir_animal"),

    # Histórico veterinário
    path("historico-veterinario/", lista_historicos, name="lista_historicos"),
    path("historico-veterinario/novo/", novo_historico, name="novo_historico"),
    path("historico-veterinario/<int:historico_id>/", detalhes_historico, name="detalhes_historico"),
    path("historico-veterinario/<int:historico_id>/editar/", editar_historico, name="editar_historico"),
    path("historico-veterinario/<int:historico_id>/excluir/", excluir_historico, name="excluir_historico"),

    # Adoções
    path("adocoes/", lista_adocoes, name="lista_adocoes"),
    path("adocoes/nova/", nova_adocao, name="nova_adocao"),
    path("adocoes/<int:adocao_id>/", detalhes_adocao, name="detalhes_adocao"),
    path("adocoes/<int:adocao_id>/editar/", editar_adocao, name="editar_adocao"),
    path("adocoes/<int:adocao_id>/excluir/", excluir_adocao, name="excluir_adocao"),
]
