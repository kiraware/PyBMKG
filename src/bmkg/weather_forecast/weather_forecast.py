from ..bmkg import BMKG
from ..enum.weather_forecast import Province
from .parser import WeatherForecastData, parse_weather_forecast_data

__all__ = ["WeatherForecast"]


class WeatherForecast(BMKG):
    url = "DataMKG/MEWS/DigitalForecast/"

    async def get_weather_forecast(self, province: Province) -> WeatherForecastData:
        response = await self.session.get(
            f"{self.base_url}{self.url}DigitalForecast-{province.value}.xml"
        )

        return parse_weather_forecast_data(await response.read())
