from aiohttp import ClientSession

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

    def __init__(self, session: ClientSession | None = None) -> None:
        API.__init__(self, session)

        self.earthquake = Earthquake(self._session)
        self.weather_forecast = WeatherForecast(self._session)
