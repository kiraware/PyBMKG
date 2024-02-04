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
