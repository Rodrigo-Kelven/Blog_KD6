from fastapi import APIRouter
from controllers.home import route_home
from controllers.artigs import router_article
from controllers.portifolio import route_portifolio
from enum import Enum

# tasgs dos endpoints
class Tags_route(Enum):
    Home = "Home"
    Artigs = "Article"
    Portifolio = "Portifolio"

# tagas do prefixo dos endpoints
class Prefix(Enum):
    api = "/api/blog/v1"
    api_auth = ""


# funcao para centralizar todas as rotas 
def all_routes(app):
    app.include_router(route_home, prefix=Prefix.api.value ,tags=[Tags_route.Home.value])
    app.include_router(router_article, prefix=Prefix.api.value, tags=[Tags_route.Artigs.value])
    app.include_router(route_portifolio, prefix=Prefix.api.value, tags=[Tags_route.Portifolio.value])




"""
(method) def include_router(
    router: APIRouter,
    *,
    prefix: str = "",
    tags: List[str | Enum] | None = None,
    dependencies: Sequence[Depends] | None = None,
    responses: Dict[int | str, Dict[str, Any]] | None = None,
    deprecated: bool | None = None,
    include_in_schema: bool = True,
    default_response_class: type[Response] = Default(JSONResponse),
    callbacks: List[BaseRoute] | None = None,
    generate_unique_id_function: (APIRoute) -> str = Default(generate_unique_id)
) -> None
"""