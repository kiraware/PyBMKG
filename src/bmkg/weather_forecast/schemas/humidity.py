from dataclasses import dataclass, field

__all__ = ["Humidity"]


@dataclass(slots=True)
class Humidity:
    """
    A schema used to store info about humidity.

    Attributes:
        percentage: percentage of humidity in % as its unit.
    """

    percentage: int = field(metadata={"unit": "%"})
