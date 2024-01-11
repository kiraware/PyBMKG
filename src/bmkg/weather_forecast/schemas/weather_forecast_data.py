from collections.abc import Iterator
from dataclasses import dataclass
from datetime import datetime

from .area import Area
from .data import Data
from .forecast import Forecast
from .weather import Weather

__all__ = ["WeatherForecastData"]


@dataclass
class WeatherForecastData:
    data: Data
    forecast: Forecast
    issue: datetime
    weathers: dict[Area, Iterator[Weather]]
