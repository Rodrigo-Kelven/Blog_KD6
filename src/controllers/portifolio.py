from fastapi import APIRouter, status


route_portifolio = APIRouter()


@route_portifolio.get(
    path="/portfolio",
    status_code=status.HTTP_200_OK,
    description="Route to portifolio",
    name="Route to portifolio"
)
async def get_portifolio():
    return "Route portifolio ok"


@route_portifolio.delete(
    path="/portfolio/{id_portifolio}/delete",
    status_code=status.HTTP_200_OK,
    description="Route to portifolio",
    name="Route to portifolio"
)
async def get_portifolio(id_portifolio: int):
    return f"Delete portifolio ID: {id_portifolio}"


@route_portifolio.post(
    path="/portfolio/create",
    status_code=status.HTTP_200_OK,
    description="Route to portifolio",
    name="Route to portifolio"
)
async def get_portifolio():
    return "Route portifolio ok"


@route_portifolio.put(
    path="/portfolio{id_portifolio}/update",
    status_code=status.HTTP_200_OK,
    description="Route to portifolio",
    name="Route to portifolio"
)
async def get_portifolio(id_portifolio: int):
    return f"Update portifolio ID: {id_portifolio}"


