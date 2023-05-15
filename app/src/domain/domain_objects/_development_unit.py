import datetime

from pydantic import BaseModel


class DevelopmentUnit(BaseModel):
    development_unit: float
    date: datetime.date
