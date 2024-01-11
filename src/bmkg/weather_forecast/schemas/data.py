from dataclasses import dataclass

__all__ = ["Data"]


@dataclass(slots=True)
class Data:
    source: str
    productioncenter: str
