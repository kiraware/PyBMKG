from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Self

from ...common.schemas import Coordinate

__all__ = ["Earthquake"]


@dataclass(slots=True)
class Earthquake:
    datetime: datetime
    coordinate: Coordinate
    magnitude: float = field(metadata={"unit": "M"})
    kedalaman: str
    wilayah: str

    @classmethod
    def from_earthquake_data(cls, earthquake_data: Earthquake, **kwargs) -> Self:
        return cls(
            earthquake_data.datetime,
            earthquake_data.coordinate,
            earthquake_data.magnitude,
            earthquake_data.kedalaman,
            earthquake_data.wilayah,
            **kwargs,
        )
