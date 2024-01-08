from traceback import TracebackException
from types import TracebackType

from aiohttp import ClientSession


class BMKG:
    base_url = "https://data.bmkg.go.id/"

    def __init__(self) -> None:
        self._session = ClientSession()

    async def __aenter__(self) -> "BMKG":
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
