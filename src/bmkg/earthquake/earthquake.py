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
        response = await self._session.get(f"{self.base_url}{self.url}autogempa.json")

        return parse_latest_earthquake_data(await response.read())

    async def get_latest_earthquake_shakemap(self, shakemap: Shakemap) -> bytes:
        response = await self._session.get(f"{self.base_url}{self.url}{shakemap}")

        return await response.read()

    async def get_strong_earthquake(self) -> Iterator[StrongEarthquake]:
        response = await self._session.get(
            f"{self.base_url}{self.url}gempaterkini.json"
        )

        return parse_strong_earthquake_data(await response.read())

    async def get_felt_earthquake(self) -> Iterator[FeltEarthquake]:
        response = await self._session.get(
            f"{self.base_url}{self.url}gempadirasakan.json"
        )

        return parse_felt_earthquake_data(await response.read())
