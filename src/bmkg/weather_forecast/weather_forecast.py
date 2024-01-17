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

        Examples:
            >>> import asyncio
            >>> async def main():
            ...     async with WeatherForecast() as weather_forecast:
            ...         weather_forecast_data = await weather_forecast.get_weather_forecast(
            ...             Province.ACEH
            ...         )
            ...         print(weather_forecast_data)
            >>> asyncio.run(main())
            WeatherForecast(data=Data(source=...)

        Args:
            A `province` enum instance.

        Returns:
            A `WeatherForecastData` schema.
        """  # noqa: E501
        async with self._session.get(
            f"{self.base_url}{self.url}DigitalForecast-{province.value}.xml"
        ) as response:
            return parse_weather_forecast_data(await response.read())
