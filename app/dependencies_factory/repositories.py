from app.src import domain
from .. import implementations


def development_unit_repository() -> domain.DevelopmentUnitRepository:
    return implementations.DevelopmentUnitImplementation()
