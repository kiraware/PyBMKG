from dataclasses import dataclass, field

from ..enums import Cardinal, Sexa

__all__ = ["WindDirection"]


@dataclass(slots=True)
class WindDirection:
    """
    A schema used to store info about wind direction.

    Attributes:
        deg: degree of a wind direction with deg as its unit.
        card: card direction of a wind direction with CARD as its unit.
        sexa: sexa direction of a wind direction with SEXA as its unit.
    """

    deg: float = field(metadata={"unit": "deg"})
    card: Cardinal = field(metadata={"unit": "CARD"})
    sexa: Sexa = field(metadata={"unit": "SEXA"})
