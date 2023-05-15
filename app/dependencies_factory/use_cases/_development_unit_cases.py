from ..repositories import development_unit_repository

from app.src.cases.development_unit import GetDevelopmentUnitByDateCase


def get_development_unit_by_date_case() -> GetDevelopmentUnitByDateCase:
    return GetDevelopmentUnitByDateCase(
        development_unit_repository=development_unit_repository()
    )
