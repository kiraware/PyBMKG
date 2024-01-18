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
    A schema used to store info about weather forecast.

    Attributes:
        data: Data schema from api.
        forecast: Forecast schema from api.
        issue: datetime of the issue.
        weathers: weather info with Area as key and iterator of Weather as value.

    Note:
        `issue` field is naive datetime, means it has no information about its
        timezone. `weathers` has an `Area` schema as it key and iterator of `Weather`
        that contain information about weather forecast of that area as it value. Only
        area type is land that has weather forecast information, whereas sea is not.
    """

    data: Data
    forecast: Forecast
    issue: datetime
    weathers: dict[Area, Iterator[Weather] | None]
