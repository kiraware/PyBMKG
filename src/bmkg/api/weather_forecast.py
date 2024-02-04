from ..enums import Province
from ..parsers import parse_weather_forecast_data
from ..schemas import WeatherForecast as WeatherForecastData
from .api import API

__all__ = ["WeatherForecast"]


class WeatherForecast(API):
    """
    Weather Forecast API Wrapper from BMKG API.
    """

    url = "/DataMKG/MEWS/DigitalForecast"

    async def get_weather_forecast(self, province: Province) -> WeatherForecastData:
        """
        Request weather forecast from weather forecast API.

        Args:
            province: A `Province` enum symbolic names (members).

        Returns:
            A `WeatherForecastData` schema.

        Examples:
            >>> import asyncio
            >>> from bmkg import BMKG
            >>> async def main():
            ...     async with BMKG() as bmkg:
            ...         weather_forecast_data = (
            ...             await bmkg.weather_forecast.get_weather_forecast(Province.ACEH)
            ...         )
            ...         print(weather_forecast_data)
            >>> asyncio.run(main())
            WeatherForecast(data=Data(source=...)
        """  # noqa: E501
        async with self._session.get(
            f"{self.url}/DigitalForecast-{province}.xml"
        ) as response:
            return parse_weather_forecast_data(await response.read())
