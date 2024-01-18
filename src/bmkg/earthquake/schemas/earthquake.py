from dataclasses import dataclass, field
from datetime import datetime

from ...common.schemas import Coordinate

__all__ = ["Earthquake"]


@dataclass(slots=True)
class Earthquake:
    """
    A schema used to store info about earthquake.

    Attributes:
        datetime: datetime of the earthquake.
        coordinate: coordinate of the earthquake.
        magnitude: magnitude of earthquake in M as its unit.
        kedalaman: depth of the earthquake in km as its unit.
        wilayah: region of the earthquake.

    Note:
        The `datetime` field is aware datetime, meaning it has the timezone information.
    """

    datetime: datetime
    coordinate: Coordinate
    magnitude: float = field(metadata={"unit": "M"})
    kedalaman: str
    wilayah: str
