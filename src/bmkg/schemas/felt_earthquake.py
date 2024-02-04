from dataclasses import dataclass

from .earthquake import Earthquake

__all__ = ["FeltEarthquake"]


@dataclass(slots=True)
class FeltEarthquake:
    """
    A schema used to store info about felt earthquake.

    Attributes:
        earthquake: earthquake schema.
        felt: area that felt an earthquake on the MMI scale.
    """

    earthquake: Earthquake
    felt: str
