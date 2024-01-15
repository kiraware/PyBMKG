from dataclasses import dataclass, field
from datetime import datetime

from ...common.schemas import Coordinate

__all__ = ["Earthquake"]


@dataclass(slots=True)
class Earthquake:
    """
    `Earthquake` schema used to store info about `datetime`, `coordinate`, `magnitude`,
    `kedalaman` and `wilayah`.

    The `datetime` field is aware datetime,
    meaning it has the timezone. The magnitude has `"M"` for its unit.
    """

    datetime: datetime
    coordinate: Coordinate
    magnitude: float = field(metadata={"unit": "M"})
    kedalaman: str
    wilayah: str
