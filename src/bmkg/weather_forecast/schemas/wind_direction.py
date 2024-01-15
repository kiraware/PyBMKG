from dataclasses import dataclass, field

from ..enums import Cardinal, Sexa

__all__ = ["WindDirection"]


@dataclass(slots=True)
class WindDirection:
    """
    `WindDirection` schema used to store info about wind direction in `deg`, `card`, and
    `sexa`.

    Note `deg` is degree. `deg` has metadata unit `"deg"`, `card` has metadata
    unit `"CARD"` and `sexa` has metadata unit `"SEXA"`.
    """

    deg: float = field(metadata={"unit": "deg"})
    card: Cardinal = field(metadata={"unit": "CARD"})
    sexa: Sexa = field(metadata={"unit": "SEXA"})
