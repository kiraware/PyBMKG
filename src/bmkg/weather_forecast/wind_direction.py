from dataclasses import dataclass, field

from .enum import Cardinal, Sexa

__all__ = ["WindDirection"]


@dataclass(slots=True)
class WindDirection:
    deg: float = field(metadata={"unit": "deg"})
    card: Cardinal = field(metadata={"unit": "CARD"})
    sexa: Sexa = field(metadata={"unit": "SEXA"})
