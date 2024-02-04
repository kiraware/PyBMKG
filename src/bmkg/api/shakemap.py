from aiohttp import ClientSession

from .. import schemas
from .api import API

__all__ = ["Shakemap"]


class Shakemap(API, schemas.Shakemap):
    """
    Shakemap API Wrapper from BMKG API.
    """

    url = "/DataMKG/TEWS"

    def __init__(self, session: ClientSession, file_name: str) -> None:
        API.__init__(self, session)
        schemas.Shakemap.__init__(self, file_name)

    async def get_content(self) -> bytes:
        """
        Get the shakemap file content.

        Returns:
            A bytes of `Shakemap` image.

        Examples:
            >>> import asyncio
            >>> from bmkg import BMKG
            >>> async def main():
            ...     async with BMKG() as bmkg:
            ...         latest_earthquake = await bmkg.earthquake.get_latest_earthquake()
            ...         shakemap = latest_earthquake.shakemap
            ...         shakemap_content = await shakemap.get_content()
            ...         print(shakemap_content)
            >>> asyncio.run(main())
            b'...'
        """  # noqa: E501
        async with self._session.get(f"{self.url}/{self.file_name}") as response:
            return await response.read()
