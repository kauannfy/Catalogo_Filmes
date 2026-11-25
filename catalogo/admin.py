from django.contrib import admin
from .models import Filme, Diretor, Categoria

admin.site.register(Filme)
admin.site.register(Diretor)
admin.site.register(Categoria)