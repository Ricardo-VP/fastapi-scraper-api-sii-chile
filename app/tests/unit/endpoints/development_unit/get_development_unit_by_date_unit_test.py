import typing

from faker import Faker
import pytest
from pytest_mock import MockerFixture


from app.src.cases import GetDevelopmentUnitByDateResponse
from app.src._development_unit import get_by_date


class TestGetDevelopmentUnitByDate:
    @pytest.fixture(name="test_data")
    def __test_data(self, mocker: MockerFixture, faker: Faker) -> typing.Any:
        return mocker.Mock(
            response=GetDevelopmentUnitByDateResponse(
                development_unit=faker.pyfloat()
            ),
            expected_date="01-05-2023"
        )

    @pytest.fixture(name="dependencies_factory")
    def __dependencies_factory(self, mocker: MockerFixture) -> typing.Callable:
        def _factory(mock_data: typing.Any) -> typing.Any:
            return mocker.Mock(use_case=mocker.AsyncMock(return_value=mock_data.response))

        return _factory

    @pytest.mark.asyncio
    async def test__includes_the_development_unit_as_part_of_the_response(
        self, test_data: typing.Any, dependencies_factory: typing.Callable
    ) -> None:
        dependencies = dependencies_factory(test_data)

        response = await get_by_date(
            expected_date=test_data.expected_date,
            get_development_unit_by_date_use_case=dependencies.use_case
        )

        assert response == test_data.response
