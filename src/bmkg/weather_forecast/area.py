from dataclasses import dataclass

from ..enum.weather_forecast import Type
from .name import Name

__all__ = ["Area"]


@dataclass(unsafe_hash=True, slots=True)
class Area:
    id: str
    latitude: float
    longitude: float
    coordinate: str
    type: Type
    region: str
    level: str
    description: str
    domain: str
    tags: str
    names: Name
