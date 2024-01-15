from ..bmkg import BMKG
from .enums import Province
from .parser import parse_weather_forecast_data
from .schemas import WeatherForecast as WeatherForecastData

__all__ = ["WeatherForecast"]


class WeatherForecast(BMKG):
    """
    Weather Forecast API Wrapper from BMKG API.
    """

    url = "DataMKG/MEWS/DigitalForecast/"

    async def get_weather_forecast(self, province: Province) -> WeatherForecastData:
        """
        Request weather forecast from weather forecast API.

        Return `WeatherForecastData`
        schema.
        """
        async with self._session.get(
            f"{self.base_url}{self.url}DigitalForecast-{province.value}.xml"
        ) as response:
            return parse_weather_forecast_data(await response.read())
