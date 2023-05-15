from ._request import GetDevelopmentUnitByDateRequest
from ._response import GetDevelopmentUnitByDateResponse
from ...domain import DevelopmentUnitRepository, DevelopmentUnit


class GetDevelopmentUnitByDateCase:
    def __init__(self, development_unit_repository: DevelopmentUnitRepository) -> None:
        self.repository = development_unit_repository

    async def __call__(
        self, request: GetDevelopmentUnitByDateRequest
    ) -> GetDevelopmentUnitByDateResponse:
        development_unit: DevelopmentUnit = await self.repository.get_by_date(
            request.expected_date
        )

        return GetDevelopmentUnitByDateResponse(
            development_unit=development_unit.development_unit
        )
