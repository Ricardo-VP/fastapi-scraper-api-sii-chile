from pydantic import BaseModel


class GetDevelopmentUnitByDateRequest(BaseModel):
    expected_date: str
