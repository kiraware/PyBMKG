from ..schemas import WeatherForecast
from ..types import WeatherForecastData
from .parse_location_data import parse_location_data
from .parse_weather_data import parse_weather_data

__all__ = ["parse_weather_forecast_data"]


def parse_weather_forecast_data(
    weather_forecast_data: WeatherForecastData,
) -> WeatherForecast:
    """
    Parse `WeatherForecastData` JSON.

    Args:
        weather_forecast_data: A dict representing JSON of weather forecast data.

    Returns:
        A `WeatherForecast` schema.
    """
    location = parse_location_data(weather_forecast_data["lokasi"])
    weathers = [
        parse_weather_data(weather)
        for weather in weather_forecast_data["data"][0]["cuaca"][0]
    ]

    return WeatherForecast(location, weathers)
