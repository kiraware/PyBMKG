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
    """
    `WeatherForecast` schema used to store info about weather forecast `data`,
    `forecast`, `issue`, and `weathers`.

    Note that `issue` is naive datetime, means it
    has no information about it's timezone. `weathers` has an `Area` schema as it key
    and iterator of `Weather` that contain information about weather forecast of that
    area as it value. Only `Area.type == Type.LAND` that has weather forecast
    information, `Type.SEA` is not.
    """

    data: Data
    forecast: Forecast
    issue: datetime
    weathers: dict[Area, Iterator[Weather] | None]
