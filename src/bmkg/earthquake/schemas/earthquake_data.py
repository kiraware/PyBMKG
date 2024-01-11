from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import Self

from ...common.schemas import Coordinate

__all__ = ["EarthquakeData"]


@dataclass(slots=True)
class EarthquakeData:
    datetime: datetime
    coordinate: Coordinate
    magnitude: float
    kedalaman: str
    wilayah: str

    @classmethod
    def from_earthquake_data(cls, earthquake_data: EarthquakeData, **kwargs) -> Self:
        return cls(
            earthquake_data.datetime,
            earthquake_data.coordinate,
            earthquake_data.magnitude,
            earthquake_data.kedalaman,
            earthquake_data.wilayah,
            **kwargs,
        )
