from dataclasses import dataclass

from .earthquake import Earthquake

__all__ = ["FeltEarthquake"]


@dataclass(slots=True)
class FeltEarthquake:
    """
    `FeltEarthquake` schema used to store info about `earthquake` and `dirasakan`.
    """

    earthquake: Earthquake
    dirasakan: str
