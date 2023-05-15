from fastapi import FastAPI

from ._middlewares import apply_middlewares
from ._exception_handlers import add_exception_handlers

from ..src import (
    development_unit_router
)


def create() -> FastAPI:
    app = FastAPI()

    apply_middlewares(app)
    add_exception_handlers(app)

    app.include_router(development_unit_router)

    return app
