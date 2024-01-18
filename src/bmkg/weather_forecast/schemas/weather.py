from dataclasses import dataclass
from datetime import datetime

from ..enums import Weather as WeatherEnum
from .humidity import Humidity
from .temperature import Temperature
from .wind_direction import WindDirection
from .wind_speed import WindSpeed

__all__ = ["Weather"]


@dataclass(slots=True)
class Weather:
    """
    A schema used to store info about weather.

    Attributes:
        datetime: datetime of a weather.
        weather: `Weather` enum symbolic names (members) of a weather condition.
        temperature: temperature of a weather.
        minimum_temperature: minimum temperature of a weather.
        maximum_temperature: maximum temperature of a weather.
        humidity: humidity of a weather.
        min_humidity: minimum humidity of a weather.
        max_humidity: maximum humidity of a weather.
        wind_direction: wind direction of a weather.
        wind_speed: wind speed of a weather.

    Note:
        `datetime` is naive datetime, means it has no information about its timezone.
        Also don't be confused with `weather`, this `weather` field is weather enum that
        has representation of weather condition.
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
