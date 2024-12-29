from datetime import datetime

from .. import enums
from ..schemas import Weather
from ..types import WeatherData

__all__ = ["parse_weather_data"]


def parse_weather_data(weather_data: WeatherData) -> Weather:
    """
    Parse `WeatherData` JSON.

    Args:
        weather_data: A dict representing JSON of weather forecast data.

    Returns:
        A `Weather` schema.
    """

    return Weather(
        datetime.fromisoformat(weather_data["datetime"]),
        int(weather_data["t"]),
        int(weather_data["tcc"]),
        float(weather_data["tp"]),
        enums.Weather(weather_data["weather"]),
        int(weather_data["wd_deg"]),
        enums.Cardinal(weather_data["wd"]),
        enums.Cardinal(weather_data["wd_to"]),
        float(weather_data["ws"]),
        int(weather_data["hu"]),
        int(weather_data["vs"]),
        weather_data["time_index"],
        datetime.fromisoformat(weather_data["analysis_date"]),
        weather_data["image"],
        datetime.strptime(weather_data["utc_datetime"], "%Y-%m-%d %H:%M:%S"),
        datetime.strptime(weather_data["local_datetime"], "%Y-%m-%d %H:%M:%S"),
    )
