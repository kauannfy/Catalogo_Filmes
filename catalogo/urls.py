from django.urls import path
from . import views

app_name = "catalogo"

urlpatterns = [
    path("", views.filmes_lista_view, name="filmes_list"),
]