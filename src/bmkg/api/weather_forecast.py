from ..parsers import parse_weather_forecast_data
from ..schemas import WeatherForecast as WeatherForecastData
from .api import API

__all__ = ["WeatherForecast"]


class WeatherForecast(API):
    """
    Weather Forecast API Wrapper from BMKG API.
    """

    base_url = "https://api.bmkg.go.id"
    url = "/publik/prakiraan-cuaca"

    async def get_weather_forecast(self, region_code: str) -> WeatherForecastData:
        """
        Request weather forecast from weather forecast API.

        Args:
            region_code: The administrative region code (level IV) for a subdistrict or village in Indonesia. The code is formatted as `W.X.Y.Z` (e.g., `"11.01.01.2001"`). You can find the list of available region codes at https://kodewilayah.id.

        Returns:
            A `WeatherForecastData` schema.

        Examples:
            >>> import asyncio
            >>> from bmkg import WeatherForecast
            >>> async def main():
            ...     async with WeatherForecast() as weather_forecast:
            ...         weather_forecast_data = await weather_forecast.get_weather_forecast(
            ...             "11.01.01.2001"
            ...         )
            ...         print(weather_forecast_data)
            >>> asyncio.run(main())
            WeatherForecast(location=Location(admin_level_1=...)
        """
        async with self._session.get(
            self.url, params={"adm4": region_code}
        ) as response:
            return parse_weather_forecast_data(await response.json())
