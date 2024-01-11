from dataclasses import dataclass

from ..common.coordinate import Coordinate
from .enums import Type
from .name import Name

__all__ = ["Area"]


@dataclass(unsafe_hash=True, slots=True)
class Area:
    id: str
    coordinate: Coordinate
    type: Type
    region: str
    level: str
    description: str
    domain: str
    tags: str
    names: Name
