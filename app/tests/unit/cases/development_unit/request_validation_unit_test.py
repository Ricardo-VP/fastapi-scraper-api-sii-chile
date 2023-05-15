from app.src.cases.development_unit import GetDevelopmentUnitByDateRequest


class TestGetDevelopmentUnitByDateRequest:
    def test__does_not_raise_an_error__when_all_validations_are_correct(
        self
    ) -> None:
        request = GetDevelopmentUnitByDateRequest(
            expected_date="01-05-2023"
        )
        assert request
