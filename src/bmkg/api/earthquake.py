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

    base_url = "https://data.bmkg.go.id"
    url = "/DataMKG/TEWS"

    async def get_latest_earthquake(self) -> schemas.LatestEarthquake:
        """
        Request latest earthquake from earthquake API.

        Returns:
            A `LatestEarthquake` schema.

        Examples:
            >>> import asyncio
            >>> from bmkg import Earthquake
            >>> async def main():
            ...     async with Earthquake() as earthquake:
            ...         latest_earthquake = await earthquake.get_latest_earthquake()
            ...         print(latest_earthquake)
            >>> asyncio.run(main())
            LatestEarthquake(earthquake=Earthquake(datetime=datetime.datetime(...)

        Notes:
            The `LatestEarthquake` schema has a `shakemap` field which is the `Shakemap` API.
        """
        async with self._session.get(f"{self.url}/autogempa.json") as response:
            latest_earthquake = parse_latest_earthquake_data(await response.json())  # type: ignore

            latest_earthquake.shakemap = Shakemap(
                latest_earthquake.shakemap.file_name, self._session
            )

            return latest_earthquake

    async def get_strong_earthquake(self) -> Iterator[schemas.StrongEarthquake]:
        """
        Request strong earthquake that has magnitude 5.0 above from earthquake API.

        Returns:
            An iterator of fifteen `StrongEarthquake` schema.

        Examples:
            >>> import asyncio
            >>> from bmkg import Earthquake
            >>> async def main():
            ...     async with Earthquake() as earthquake:
            ...         strong_earthquake = await earthquake.get_strong_earthquake()
            ...         print(strong_earthquake)
            >>> asyncio.run(main())
            <generator object parse_strong_earthquake_data at ...>
        """
        async with self._session.get(f"{self.url}/gempaterkini.json") as response:
            return parse_strong_earthquake_data(await response.json())  # type: ignore

    async def get_felt_earthquake(self) -> Iterator[schemas.FeltEarthquake]:
        """
        Request felt earthquake from earthquake API.

        Returns:
            An iterator of fifteen `FeltEarthquake` schema.

        Examples:
            >>> import asyncio
            >>> from bmkg import Earthquake
            >>> async def main():
            ...     async with Earthquake() as earthquake:
            ...         felt_earthquake = await earthquake.get_felt_earthquake()
            ...         print(felt_earthquake)
            >>> asyncio.run(main())
            <generator object parse_felt_earthquake_data at ...>
        """
        async with self._session.get(f"{self.url}/gempadirasakan.json") as response:
            return parse_felt_earthquake_data(await response.json())  # type: ignore
