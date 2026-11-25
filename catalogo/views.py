from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Filme, Diretor, Categoria


def lista_filmes(request):
    busca = request.GET.get("q", "").strip()
    diretor_id = request.GET.get("diretor", "")
    categoria_id = request.GET.get("categoria", "")

    filmes = Filme.objects.select_related("diretor", "categoria")

    if busca:
        filmes = filmes.filter(titulo__icontains=busca)
    if diretor_id.isdigit():
        filmes = filmes.filter(diretor_id=diretor_id)
    if categoria_id.isdigit():
        filmes = filmes.filter(categoria_id=categoria_id)

    paginator = Paginator(filmes, 5)
    page_obj = paginator.get_page(request.GET.get("page"))

    params = request.GET.copy()
    params.pop("page", None)

    context = {
        "page_obj": page_obj,
        "paginator": paginator,
        "diretores": Diretor.objects.all(),
        "categorias": Categoria.objects.all(),
        "busca": busca,
        "diretor_id": diretor_id,
        "categoria_id": categoria_id,
        "querystring": params.urlencode(),
    }
    return render(request, "catalogo/lista_filmes.html", context)