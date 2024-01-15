from dataclasses import dataclass

__all__ = ["Forecast"]


@dataclass(slots=True)
class Forecast:
    """
    `Forecast` schema used to store info about `domain`.
    """

    domain: str
