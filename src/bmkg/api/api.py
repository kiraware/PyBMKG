from traceback import TracebackException
from types import TracebackType
from typing import Self

from aiohttp import ClientSession

__all__ = ["API"]


class API:
    """
    Base API class.
    """

    def __init__(self, session: ClientSession | None = None) -> None:
        self._session = (
            session if session is not None else ClientSession("https://data.bmkg.go.id")
        )

    async def __aenter__(self) -> Self:
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
