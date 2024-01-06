from dataclasses import dataclass

from ..enum.weather_forecast import Cardinal, Sexa

__all__ = ["WindDirection"]


@dataclass(slots=True)
class WindDirection:
    deg: float
    card: Cardinal
    sexa: Sexa
