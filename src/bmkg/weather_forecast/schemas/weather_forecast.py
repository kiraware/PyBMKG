from collections.abc import Iterator
from dataclasses import dataclass
from datetime import datetime

from .area import Area
from .data import Data
from .forecast import Forecast
from .weather import Weather

__all__ = ["WeatherForecast"]


@dataclass
class WeatherForecast:
    data: Data
    forecast: Forecast
    issue: datetime
    weathers: dict[Area, Iterator[Weather]]
