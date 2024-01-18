from dataclasses import dataclass

from ..types import Shakemap
from .earthquake import Earthquake

__all__ = ["LatestEarthquake"]


@dataclass(slots=True)
class LatestEarthquake:
    """
    A schema used to store info about latest earthquake.

    Attributes:
        earthquake: earthquake schema.
        potensi: potency of latest earthquake.
        dirasakan: zone of latest earthquake.
        shakemap: shakemap file name of latest earthquake.
    """

    earthquake: Earthquake
    potensi: str
    dirasakan: str
    shakemap: Shakemap
