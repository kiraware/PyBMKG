from dataclasses import dataclass

from .name import Name

__all__ = ["Area"]


@dataclass(unsafe_hash=True, slots=True)
class Area:
    id: str
    latitude: str
    longitude: str
    coordinate: str
    type: str
    region: str
    level: str
    description: str
    domain: str
    tags: str
    names: Name
