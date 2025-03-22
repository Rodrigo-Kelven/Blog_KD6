from fastapi import FastAPI
from controllers.all_routes import all_routes
import logging

app = FastAPI(
    title="API Blog in FastAPI",
    version="1.0.2",
    description="Api of Blog and portifolio",
    debug=True,
    docs_url="/docs",
    redirect_slashes=True,
    redoc_url="/redoc",
    )

@app.on_event("startup")
async def startup():
    logging.info(
        msg="Aplicacao inicializando..."
    )
    # funcao centralizadora de rotas do projeto
    all_routes(app)