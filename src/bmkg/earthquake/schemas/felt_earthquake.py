from dataclasses import dataclass

from .earthquake import Earthquake

__all__ = ["FeltEarthquake"]


@dataclass(slots=True)
class FeltEarthquake(Earthquake):
    dirasakan: str
