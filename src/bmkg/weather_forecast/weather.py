from dataclasses import dataclass
from datetime import datetime

from ..enum.weather_forecast import Weather as WeatherEnum
from .humidity import Humidity
from .temperature import Temperature
from .wind_direction import WindDirection
from .wind_speed import WindSpeed

__all__ = ["Weather"]


@dataclass(slots=True)
class Weather:
    """
    Class that represent Weather object.
    """

    datetime: datetime
    weather: WeatherEnum
    temperature: Temperature
    minimum_temperature: Temperature
    maximum_temperature: Temperature
    humidity: Humidity
    min_humidity: Humidity
    max_humidity: Humidity
    wind_direction: WindDirection
    wind_speed: WindSpeed
