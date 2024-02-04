from collections.abc import Iterator

from .. import schemas
from ..parsers import (
    parse_felt_earthquake_data,
    parse_latest_earthquake_data,
    parse_strong_earthquake_data,
)
from .api import API
from .shakemap import Shakemap

__all__ = ["Earthquake"]


class Earthquake(API):
    """
    Earthquake API Wrapper from BMKG API.
    """

    url = "/DataMKG/TEWS"

    async def get_latest_earthquake(self) -> schemas.LatestEarthquake:
        """
        Request latest earthquake from earthquake API.

        Returns:
            A `LatestEarthquake` schema.

        Examples:
            >>> import asyncio
            >>> from bmkg import BMKG
            >>> async def main():
            ...     async with BMKG() as bmkg:
            ...         latest_earthquake = await bmkg.earthquake.get_latest_earthquake()
            ...         print(latest_earthquake)
            >>> asyncio.run(main())
            LatestEarthquake(earthquake=Earthquake(datetime=datetime.datetime(...)

        Notes:
            The `LatestEarthquake` schema has a `shakemap` field which is the `Shakemap` API.
        """  # noqa: E501
        async with self._session.get(f"{self.url}/autogempa.json") as response:
            latest_earthquake = parse_latest_earthquake_data(await response.json())  # type: ignore

            latest_earthquake.shakemap = Shakemap(
                self._session, latest_earthquake.shakemap.file_name
            )

            return latest_earthquake

    async def get_strong_earthquake(self) -> Iterator[schemas.StrongEarthquake]:
        """
        Request strong earthquake that has magnitude 5.0 above from earthquake API.

        Returns:
            An iterator of fifteen `StrongEarthquake` schema.

        Examples:
            >>> import asyncio
            >>> from bmkg import BMKG
            >>> async def main():
            ...     async with BMKG() as bmkg:
            ...         strong_earthquake = await bmkg.earthquake.get_strong_earthquake()
            ...         print(strong_earthquake)
            >>> asyncio.run(main())
            <generator object parse_strong_earthquake_data at ...>
        """  # noqa: E501
        async with self._session.get(f"{self.url}/gempaterkini.json") as response:
            return parse_strong_earthquake_data(await response.json())  # type: ignore

    async def get_felt_earthquake(self) -> Iterator[schemas.FeltEarthquake]:
        """
        Request felt earthquake from earthquake API.

        Returns:
            An iterator of fifteen `FeltEarthquake` schema.

        Examples:
            >>> import asyncio
            >>> from bmkg import BMKG
            >>> async def main():
            ...     async with BMKG() as bmkg:
            ...         felt_earthquake = await bmkg.earthquake.get_felt_earthquake()
            ...         print(felt_earthquake)
            >>> asyncio.run(main())
            <generator object parse_felt_earthquake_data at ...>
        """
        async with self._session.get(f"{self.url}/gempadirasakan.json") as response:
            return parse_felt_earthquake_data(await response.json())  # type: ignore
