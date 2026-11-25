from django.core.paginator import Paginator
from django.shortcuts import render

from . import models


def filmes_lista_view(request):
    busca = request.GET.get("busca", "").strip()
    diretor = request.GET.get("diretor", "")
    categoria = request.GET.get("categoria", "")

    filmes = models.Filme.objects.all()

    if request.method == "GET":
        if busca:
            filmes = filmes.filter(titulo__icontains=busca)
        if diretor:
            filmes = filmes.filter(diretor__id=diretor)
        if categoria:
            filmes = filmes.filter(categoria__id=categoria)

    filmes = filmes.order_by("titulo", "id")

    paginator = Paginator(filmes, 5)
    numero_pagina = request.GET.get("page")
    page_obj = paginator.get_page(numero_pagina)

    return render(request, "filme/lista.html", {
        "page_obj": page_obj,
        "diretores": models.Diretor.objects.all(),
        "categorias": models.Categoria.objects.all(),
        "busca": busca,
        "diretor_selecionado": diretor,
        "categoria_selecionada": categoria,
    })
