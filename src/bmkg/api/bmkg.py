from traceback import TracebackException
from types import TracebackType
from typing import Self

from .api import API
from .earthquake import Earthquake
from .weather_forecast import WeatherForecast

__all__ = ["BMKG"]


class BMKG(API):
    """
    Base BMKG API wrapper.

    Attributes:
        earthquake (Earthquake): earthquake api interface.
        weather_forecast (WeatherForecast): weather forecast api interface.
    """

    def __init__(self) -> None:
        API.__init__(self)

        self.earthquake = Earthquake(self._session)
        self.weather_forecast = WeatherForecast(self._session)

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
