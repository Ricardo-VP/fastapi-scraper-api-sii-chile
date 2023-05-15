import traceback

from fastapi import FastAPI, Request, status

from fastapi.responses import JSONResponse


from app.src.exceptions import (
    DevelopmentUnitRepositoryError
)


async def temporary_generic_exception_handler(_request: Request, exc: Exception) -> JSONResponse:
    msg = "".join(traceback.format_exception(type(exc), exc, exc.__traceback__))

    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={"traceback": msg, "detail": exc.args},
    )


def add_exception_handlers(app: FastAPI) -> None:
    app.exception_handler(DevelopmentUnitRepositoryError)(temporary_generic_exception_handler)
