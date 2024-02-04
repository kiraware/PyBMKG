from dataclasses import dataclass

from .earthquake import Earthquake
from .shakemap import Shakemap

__all__ = ["LatestEarthquake"]


@dataclass(slots=True)
class LatestEarthquake:
    """
    A schema used to store info about latest earthquake.

    Attributes:
        earthquake: earthquake schema.
        potency: potential tsunami or not, and the status of the earthquake felt.
        felt: area that felt an earthquake on the MMI scale.
        shakemap: shakemap schema.
    """

    earthquake: Earthquake
    potency: str
    felt: str
    shakemap: Shakemap
