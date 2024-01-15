from dataclasses import dataclass

from ..types import Shakemap
from .earthquake import Earthquake

__all__ = ["LatestEarthquake"]


@dataclass(slots=True)
class LatestEarthquake:
    """
    `LatestEarthquake` schema used to store info about `earthquake`.

    `potensi`,
    `dirasakan`, and `shakemap`.
    """

    earthquake: Earthquake
    potensi: str
    dirasakan: str
    shakemap: Shakemap
