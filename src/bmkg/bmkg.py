from traceback import TracebackException
from types import TracebackType
from typing import Self

from aiohttp import ClientSession


class BMKG:
    """
    Base BMKG API wrapper.
    """

    async def __aenter__(self) -> Self:
        self._session = ClientSession("https://data.bmkg.go.id")

        return self

    async def __aexit__(
        self,
        exc_type: Exception,
        exc_val: TracebackException,
        traceback: TracebackType,
    ) -> None:
        await self.close()

    async def close(self) -> None:
        await self._session.close()
