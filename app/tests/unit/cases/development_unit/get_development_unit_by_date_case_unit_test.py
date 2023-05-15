import typing

from faker import Faker
import pytest
from pytest_mock import MockerFixture

from app.src.cases.development_unit import (
    GetDevelopmentUnitByDateCase,
    GetDevelopmentUnitByDateResponse,
    GetDevelopmentUnitByDateRequest
)


class TestGetDevelopmentUnitByDate:
    @pytest.fixture(name="test_data")
    def __test_data(
        self,
        faker: Faker,
        mocker: MockerFixture
    ) -> typing.Any:
        return mocker.Mock(
            development_unit=GetDevelopmentUnitByDateResponse(
                development_unit=faker.pyfloat()
            ),
            expected_date="01-05-2023"
        )

    @pytest.fixture(name="dependencies_factory")
    def __dependencies(self, mocker):
        def _factory(mock_data: typing.Dict = {}) -> typing.Dict:
            return {
                "development_unit_repository": mocker.Mock(
                    get_by_date=mocker.AsyncMock(return_value=mock_data.get("development_unit")),
                ),
            }

        return _factory

    @pytest.mark.asyncio
    async def test__returns_a_development_unit__given_a_date(
        self,
        test_data: typing.Callable,
        dependencies_factory: typing.Callable,
    ) -> None:
        dependencies = dependencies_factory(
            mock_data={"development_unit": test_data.development_unit}
        )

        get_development_unit_by_date_case = GetDevelopmentUnitByDateCase(**dependencies)
        response = await get_development_unit_by_date_case(
            request=GetDevelopmentUnitByDateRequest(
                expected_date=test_data.expected_date
            )
        )

        assert response == test_data.development_unit
        dependencies["development_unit_repository"].get_by_date.assert_called_once_with(
            test_data.expected_date
        )
