from pydantic import BaseModel


class GetDevelopmentUnitByDateResponse(BaseModel):
    development_unit: float
