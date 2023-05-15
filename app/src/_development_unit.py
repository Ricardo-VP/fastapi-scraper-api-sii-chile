from fastapi import APIRouter, Depends

from app.dependencies_factory.use_cases import get_development_unit_by_date_case

from .cases import (
    GetDevelopmentUnitByDateRequest,
    GetDevelopmentUnitByDateResponse,
    GetDevelopmentUnitByDateCase
)

development_unit_router = APIRouter()


@development_unit_router.get(
    "/development-unit/{expected_date}",
    response_model=GetDevelopmentUnitByDateResponse
)
async def get_by_date(
        expected_date: str,
        get_development_unit_by_date_use_case: GetDevelopmentUnitByDateCase = Depends(
            get_development_unit_by_date_case
        )):
    return await get_development_unit_by_date_use_case(
        request=GetDevelopmentUnitByDateRequest(
            expected_date=expected_date
        )
    )
