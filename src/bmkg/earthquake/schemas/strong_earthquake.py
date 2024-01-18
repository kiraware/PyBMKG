from dataclasses import dataclass

from .earthquake import Earthquake

__all__ = ["StrongEarthquake"]


@dataclass(slots=True)
class StrongEarthquake:
    """
    A schema used to store info about strong earthquake.

    Attributes:
        earthquake: earthquake schema.
        potensi: potency of latest earthquake.
    """

    earthquake: Earthquake
    potensi: str
