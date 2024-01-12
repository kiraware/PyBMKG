from dataclasses import dataclass

from .earthquake import Earthquake

__all__ = ["StrongEarthquake"]


@dataclass(slots=True)
class StrongEarthquake:
    earthquake: Earthquake
    potensi: str
