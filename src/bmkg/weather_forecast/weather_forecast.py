from ..bmkg import BMKG
from .enum import Province
from .parser import parse_weather_forecast_data
from .weather_forecast_data import WeatherForecastData

__all__ = ["WeatherForecast"]


class WeatherForecast(BMKG):
    url = "DataMKG/MEWS/DigitalForecast/"

    async def get_weather_forecast(self, province: Province) -> WeatherForecastData:
        response = await self._session.get(
            f"{self.base_url}{self.url}DigitalForecast-{province.value}.xml"
        )

        return parse_weather_forecast_data(await response.read())