import abc

from ..domain_objects import DevelopmentUnit


class DevelopmentUnitRepository(abc.ABC):
    @abc.abstractmethod
    async def get_by_date(
        self,
        expected_date: str
    ) -> DevelopmentUnit:
        pass
