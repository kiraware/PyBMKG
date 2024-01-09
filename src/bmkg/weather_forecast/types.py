from datetime import datetime
from typing import Iterator, Literal, TypedDict

from .enum import Weather
from .humidity import Humidity
from .temperature import Temperature
from .wind_direction import WindDirection
from .wind_speed import WindSpeed

__all__ = [
    "WeatherForecastParameter",
    "WeatherForecastParameterId",
    "WeatherForecastParameters",
]


class WeatherForecastParameters(TypedDict, total=False):
    datetime: Iterator[datetime]
    hu: Iterator[Humidity]
    humax: Iterator[Humidity]
    humin: Iterator[Humidity]
    t: Iterator[Temperature]
    tmax: Iterator[Temperature]
    tmin: Iterator[Temperature]
    weather: Iterator[Weather]
    wd: Iterator[WindDirection]
    ws: Iterator[WindSpeed]


WeatherForecastParameter = (
    Iterator[datetime]
    | Iterator[Humidity]
    | Iterator[Temperature]
    | Iterator[Weather]
    | Iterator[WindDirection]
    | Iterator[WindSpeed]
)

WeatherForecastParameterId = Literal[
    "datetime", "hu", "humax", "humin", "t", "tmax", "tmin", "weather", "wd", "ws"
]
