from collections.abc import Iterator

from ..bmkg import BMKG
from .parser import (
    parse_felt_earthquake_data,
    parse_latest_earthquake_data,
    parse_strong_earthquake_data,
)
from .schemas import (
    FeltEarthquake,
    LatestEarthquake,
    StrongEarthquake,
)
from .types import Shakemap

__all__ = ["Earthquake"]


class Earthquake(BMKG):
    url = "DataMKG/TEWS/"

    async def get_latest_earthquake(self) -> LatestEarthquake:
        async with self._session.get(
            f"{self.base_url}{self.url}autogempa.json"
        ) as response:
            return parse_latest_earthquake_data(await response.json())

    async def get_latest_earthquake_shakemap(self, shakemap: Shakemap) -> bytes:
        async with self._session.get(
            f"{self.base_url}{self.url}{shakemap}"
        ) as response:
            return await response.read()

    async def get_strong_earthquake(self) -> Iterator[StrongEarthquake]:
        async with self._session.get(
            f"{self.base_url}{self.url}gempaterkini.json"
        ) as response:
            return parse_strong_earthquake_data(await response.json())

    async def get_felt_earthquake(self) -> Iterator[FeltEarthquake]:
        async with self._session.get(
            f"{self.base_url}{self.url}gempadirasakan.json"
        ) as response:
            return parse_felt_earthquake_data(await response.json())
