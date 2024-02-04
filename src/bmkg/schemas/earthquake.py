from dataclasses import dataclass, field
from datetime import datetime

from .coordinate import Coordinate

__all__ = ["Earthquake"]


@dataclass(slots=True)
class Earthquake:
    """
    A schema used to store info about earthquake.

    Attributes:
        datetime: datetime of the earthquake.
        coordinate: coordinate of the earthquake.
        magnitude: magnitude is the strength of an earthquake in M as its unit.
        depth: depth of the earthquake in km as its unit.
        region: The area closest to the location of the earthquake epicenter.

    Note:
        The `datetime` field is aware datetime, meaning it has the timezone information.
    """

    datetime: datetime
    coordinate: Coordinate
    magnitude: float = field(metadata={"unit": "M"})
    depth: float = field(metadata={"unit": "km"})
    region: str
