from dataclasses import dataclass

__all__ = ["Forecast"]


@dataclass(slots=True)
class Forecast:
    domain: str
