from fastapi import FastAPI
from controllers.all_routes import all_routes


app = FastAPI(
    title="API Blog in FastAPI",
    version="1.0.0",
    description="Api of Blog and portifolio",
    debug=True,
    docs_url="/docs",
    redirect_slashes=True,
    redoc_url="/redoc",
    )
all_routes(app)