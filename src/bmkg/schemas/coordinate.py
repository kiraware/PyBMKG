from dataclasses import dataclass

__all__ = ["Coordinate"]


@dataclass(unsafe_hash=True, slots=True)
class Coordinate:
    """
    A schema used to store info about coordinate.

    Attributes:
        latitude: latitude of the coordinate.
        longitude: longitude of the coordinate.
    """

    latitude: float
    longitude: float
