from dataclasses import dataclass

__all__ = ["Coordinate"]


@dataclass(unsafe_hash=True, slots=True)
class Coordinate:
    """
    Coordinate schema used to store info about latitude and longitude.
    """

    latitude: float
    longitude: float
