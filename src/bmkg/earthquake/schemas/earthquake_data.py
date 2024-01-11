from __future__ import annotations

from dataclasses import asdict, dataclass
from datetime import datetime
from typing import Self

from ...common.coordinate import Coordinate

__all__ = ["EarthquakeData"]


@dataclass(slots=True)
class EarthquakeData:
    datetime: datetime
    coordinate: Coordinate
    magnitude: float
    kedalaman: str
    wilayah: str

    @classmethod
    def from_instance(cls, instance: EarthquakeData, **kwargs) -> Self:
        return cls(**asdict(instance), **kwargs)
