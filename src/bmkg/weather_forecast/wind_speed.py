from dataclasses import dataclass

__all__ = ["WindSpeed"]


@dataclass(slots=True)
class WindSpeed:
    knot: float
    mph: float
    kph: float
    ms: float
