from dataclasses import dataclass

__all__ = ["Forecast"]


@dataclass(slots=True)
class Forecast:
    """
    A schema used to store info about forecast.

    Attributes:
        domain: domain of a forecast.
    """

    domain: str
