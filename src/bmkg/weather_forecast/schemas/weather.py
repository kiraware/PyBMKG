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
    `Weather` schema used to store info about weather.

    There are `datetime`, `weather`,
    `temperature`, `minimum_temperature`, `maximum_temperature`, `humidity`,
    `min_humidity`, `max_humidity`, `wind_direction`,  and `wind_speed`. Note that
    `datetime` is naive datetime, means it has no information about it's timezone. Also
    don't be confused with `weather`, this `weather` field is weather enum that has
    representation of weather condition.
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
