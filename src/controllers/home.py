from fastapi import APIRouter, status

route_home = APIRouter()


@route_home.get(
    path="/",
    status_code=status.HTTP_200_OK,
    description="Route home",
    name="Route Home"
)
async def home():
    return "API Rodando!"


@route_home.get(
    path="/sobre",
    status_code=status.HTTP_200_OK,
    description="Route about of blog",
    name="Route about blog"
)
async def about_blog():
    return "Route about blog"