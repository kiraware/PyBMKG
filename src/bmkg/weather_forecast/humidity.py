from dataclasses import dataclass

__all__ = ["Humidity"]


@dataclass(slots=True)
class Humidity:
    percentage: int
