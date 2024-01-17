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
    """
    Earthquake API Wrapper from BMKG API.
    """

    url = "DataMKG/TEWS/"

    async def get_latest_earthquake(self) -> LatestEarthquake:
        """
        Request latest earthquake from earthquake API.

        Examples:
            >>> import asyncio
            >>> async def main():
            ...     async with Earthquake() as earthquake:
            ...         latest_earthquake = await earthquake.get_latest_earthquake()
            ...         print(latest_earthquake)
            >>> asyncio.run(main())
            LatestEarthquake(earthquake=Earthquake(datetime=datetime.datetime(...)

        Returns:
            A `LatestEarthquake` schema.
        """
        async with self._session.get(
            f"{self.base_url}{self.url}autogempa.json"
        ) as response:
            return parse_latest_earthquake_data(await response.json())

    async def get_latest_earthquake_shakemap(self, shakemap: Shakemap) -> bytes:
        """
        Request latest earthquake shakemap from earthquake API.

        Examples:
            >>> import asyncio
            >>> async def main():
            ...     async with Earthquake() as earthquake:
            ...         latest_earthquake = await earthquake.get_latest_earthquake()
            ...         shakemap = await earthquake.get_latest_earthquake_shakemap(
            ...             latest_earthquake.shakemap
            ...         )
            ...         print(shakemap)
            >>> asyncio.run(main())
            b'...'

        Args:
            A `shakemap` file name.

        Returns:
            A bytes of `shakemap` image.
        """
        async with self._session.get(
            f"{self.base_url}{self.url}{shakemap}"
        ) as response:
            return await response.read()

    async def get_strong_earthquake(self) -> Iterator[StrongEarthquake]:
        """
        Request strong earthquake that has magnitude 5.0 above from earthquake API.

        Examples:
            >>> import asyncio
            >>> async def main():
            ...     async with Earthquake() as earthquake:
            ...         strong_earthquake = await earthquake.get_strong_earthquake()
            ...         print(strong_earthquake)
            >>> asyncio.run(main())
            <generator object parse_strong_earthquake_data at ...>

        Returns:
            An iterator of fifteen `StrongEarthquake` schema that has magnitude 5.0
            above.
        """
        async with self._session.get(
            f"{self.base_url}{self.url}gempaterkini.json"
        ) as response:
            return parse_strong_earthquake_data(await response.json())

    async def get_felt_earthquake(self) -> Iterator[FeltEarthquake]:
        """
        Request felt earthquake from earthquake API.

        Examples:
            >>> import asyncio
            >>> async def main():
            ...     async with Earthquake() as earthquake:
            ...         felt_earthquake = await earthquake.get_felt_earthquake()
            ...         print(felt_earthquake)
            >>> asyncio.run(main())
            <generator object parse_felt_earthquake_data at ...>

        Returns:
            An iterator of fifteen `FeltEarthquake` schema.
        """
        async with self._session.get(
            f"{self.base_url}{self.url}gempadirasakan.json"
        ) as response:
            return parse_felt_earthquake_data(await response.json())
