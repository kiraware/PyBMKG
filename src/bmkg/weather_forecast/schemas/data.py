from dataclasses import dataclass

__all__ = ["Data"]


@dataclass(slots=True)
class Data:
    """
    `Data` schema used to store info about `source` and `productioncenter`.
    """

    source: str
    productioncenter: str
