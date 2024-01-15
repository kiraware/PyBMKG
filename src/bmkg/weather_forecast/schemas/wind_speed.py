from dataclasses import dataclass, field

__all__ = ["WindSpeed"]


@dataclass(slots=True)
class WindSpeed:
    """
    `WindSpeed` schema used to store info about wind speed in `knot`, `mph`, `kph`, and
    `ms`.

    `knot` has metadata unit `"kn"`, `mph` has metadata unit `"mph"`, `kph` has
    metadata unit `"km/h"`, and `ms` has metadata unit `"m/s"`.
    """

    knot: float = field(metadata={"unit": "kn"})
    mph: float = field(metadata={"unit": "mph"})
    kph: float = field(metadata={"unit": "km/h"})
    ms: float = field(metadata={"unit": "m/s"})
