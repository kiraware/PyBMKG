from dataclasses import dataclass

__all__ = ["Coordinate"]


@dataclass(unsafe_hash=True, slots=True)
class Coordinate:
    latitude: float
    longitude: float
