from dataclasses import dataclass, field

__all__ = ["WindSpeed"]


@dataclass(slots=True)
class WindSpeed:
    """
    A schema used to store info about wind speed.

    Attributes:
        knot: knot of a wind speed with kn as its unit.
        mph: mph of a wind speed with mph as its unit.
        kph: kph of a wind speed with km/h as its unit.
        ms: ms of a wind speed with m/s as its unit.
    """

    knot: float = field(metadata={"unit": "kn"})
    mph: float = field(metadata={"unit": "mph"})
    kph: float = field(metadata={"unit": "km/h"})
    ms: float = field(metadata={"unit": "m/s"})
