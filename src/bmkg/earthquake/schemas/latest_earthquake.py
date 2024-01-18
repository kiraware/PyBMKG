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
        potency: potency of latest earthquake.
        felt: zone of latest earthquake.
        shakemap: shakemap file name of latest earthquake.
    """

    earthquake: Earthquake
    potency: str
    felt: str
    shakemap: Shakemap
