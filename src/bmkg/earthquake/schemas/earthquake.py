from dataclasses import dataclass, field
from datetime import datetime

from ...common.schemas import Coordinate

__all__ = ["Earthquake"]


@dataclass(slots=True)
class Earthquake:
    datetime: datetime
    coordinate: Coordinate
    magnitude: float = field(metadata={"unit": "M"})
    kedalaman: str
    wilayah: str
