# Rolo de Fita

Aplicação em Django para consultar um catálogo de filmes internacionais.

## Dupla 14
- José Fernandes Figueiredo Filho
- Anderson Cauã

## Tema
Catálogo de Filmes, com os modelos Filme, Diretor e Categoria. Cada filme está relacionado a um diretor e a uma categoria.

## Filtros implementados
- **Pesquisa por título** (parâmetro `busca`): mostra os filmes cujo título contém o texto digitado, usando `titulo__icontains`.
- **Diretor** (parâmetro `diretor`): um `<select>` com os diretores cadastrados. Mostra apenas os filmes do diretor escolhido, usando `diretor__id`.
- **Categoria** (parâmetro `categoria`): um `<select>` com as categorias cadastradas. Mostra apenas os filmes da categoria escolhida, usando `categoria__id`.

Os filtros usam o método GET, funcionam sozinhos ou combinados e são aplicados antes da paginação.

Exemplo com os filtros combinados: `/?busca=origem&diretor=1&categoria=3`

## Paginação
Usa a classe `Paginator`, com 5 filmes por página. Mostra a página atual, o total de páginas e os links Anterior e Próxima, preservando a pesquisa e os filtros.

## Como executar
É necessário ter o Python 3.10 ou superior.

```
git clone https://github.com/kauannfy/Catalogo_Filmes.git
cd Catalogo_Filmes
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py runserver
```

No Windows, troque `python3 -m venv venv` por `py -m venv venv` e `source venv/bin/activate` por `venv\Scripts\activate`.

Depois, acesse http://127.0.0.1:8000/

O banco de dados com os registros já está incluído no repositório.

## Captura de tela
Listagem filtrada pela categoria Ficção Científica, na página 2:

![Listagem com filtros e paginação](docs/listagem.png)
