from dataclasses import dataclass

from .location import Location
from .weather import Weather

__all__ = ["WeatherForecast"]


@dataclass(slots=True)
class WeatherForecast:
    """
    A schema used to store information about weather forecast.

    Attributes:
        location: location information.
        weathers: list of weather forecast data.
    """

    location: Location
    weathers: list[Weather]
