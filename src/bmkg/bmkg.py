import asyncio

from aiohttp import ClientSession


class BMKG:
    base_url = "https://data.bmkg.go.id/"

    def __init__(self):
        self._create_session()

    def __del__(self):
        try:
            loop = asyncio.get_event_loop()
            asyncio.create_task(self._close_session())
        except RuntimeError:
            loop = asyncio.new_event_loop()
            loop.run_until_complete(self._close_session())

    async def _close_session(self):
        if not self.session.closed:
            await self.session.close()

    def _create_session(self):
        self.session = ClientSession()
