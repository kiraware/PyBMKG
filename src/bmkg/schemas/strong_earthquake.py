from dataclasses import dataclass

from .earthquake import Earthquake

__all__ = ["StrongEarthquake"]


@dataclass(slots=True)
class StrongEarthquake:
    """
    A schema used to store info about strong earthquake.

    Attributes:
        earthquake: earthquake schema.
        potency: potential tsunami or not, and the status of the earthquake felt.
    """

    earthquake: Earthquake
    potency: str
