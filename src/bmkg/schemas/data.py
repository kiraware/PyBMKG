from dataclasses import dataclass

__all__ = ["Data"]


@dataclass(slots=True)
class Data:
    """
    A schema used to store info about data.

    Attributes:
        source: source of a data.
        productioncenter: production center of a data.
    """

    source: str
    productioncenter: str
