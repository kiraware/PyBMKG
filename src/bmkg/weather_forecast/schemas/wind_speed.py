from dataclasses import dataclass, field

__all__ = ["WindSpeed"]


@dataclass(slots=True)
class WindSpeed:
    knot: float = field(metadata={"unit": "kn"})
    mph: float = field(metadata={"unit": "mph"})
    kph: float = field(metadata={"unit": "km/h"})
    ms: float = field(metadata={"unit": "m/s"})
