from datetime import date, datetime

from bs4 import BeautifulSoup
from urllib.request import urlopen

from app.src.domain import (
    DevelopmentUnitRepository,
    DevelopmentUnit
)

from app.src.exceptions import DevelopmentUnitRepositoryError

_MONTHS = [
    'enero',
    'febrero',
    'marzo',
    'abril',
    'mayo',
    'junio',
    'julio',
    'agosto',
    'septiembre',
    'octubre',
    'noviembre',
    'diciembre'
]

_URL = "https://www.sii.cl/valores_y_fechas/uf/uf{}.htm"
_DATE_FORMAT = "%d-%m-%Y"


class DevelopmentUnitImplementation(DevelopmentUnitRepository):
    async def get_by_date(self, expected_date: str) -> DevelopmentUnit:
        try:
            date = datetime.strptime(expected_date, _DATE_FORMAT).date()
            return DevelopmentUnit(
                date=date,
                development_unit=self.__scrape_development_unit(
                    expected_date=date
                ),
            )
        except (ValueError):
            raise DevelopmentUnitRepositoryError(
                f'An error ocurred with the date: {expected_date}. Try with another one.'
            )

    def __scrape_development_unit(self, expected_date: date) -> float:
        try:
            PAGE = urlopen(_URL.format(expected_date.year))
            HTML = PAGE.read().decode("utf-8")
            SOUP = BeautifulSoup(HTML, "html.parser")

            month = self.__get_spanish_month_name(expected_date=expected_date)
            table = SOUP.select_one(f"#mes_{month} table")
            rows = table.find_all('tr')[1:]

            for row in rows:
                data_row = row.find_all(['th', 'td'])

                for i in range(0, len(data_row), 2):
                    day = int(data_row[i].text.strip())
                    value = data_row[i+1].text.strip().replace('.', '').replace(',', '.')

                    if ((day and value) and day == expected_date.day):
                        return float(value)
        except (ValueError):
            return DevelopmentUnitRepositoryError(
                'An error ocurred while scraping the development unit value'
            )

    def __get_spanish_month_name(self, expected_date: date) -> str:
        return _MONTHS[expected_date.month-1]
