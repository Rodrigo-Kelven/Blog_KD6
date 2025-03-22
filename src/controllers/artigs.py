from fastapi import APIRouter, status



router_article = APIRouter()


@router_article.get(
    path="/articles",
    status_code=status.HTTP_200_OK,
    description="Listagem de todos os artigos",
    name="Route get all artigs with limit"
)
async def get_all_artigs():
    return "Route ok"


@router_article.post(
    path="/article/create",
    description="Postagens de artigos com base no usuário",
    name="Route register artigs"
)
async def register_artigs():
    return "Route ok"


@router_article.delete(
    path="/article/{id_artigo}/delete/",
    description="Postagens de artigos com base no usuário",
    name="Route register article"
)
async def register_artigs(id_artigo: int):
    return f"Article {id_artigo} deleted"



@router_article.put(
    path="/article/{id_artigo}/update/",
    description="Postagens de artigos com base no usuário",
    name="Route register article"
)
async def register_artigs(id_artigo: int):
    return f"Article {id_artigo} update"