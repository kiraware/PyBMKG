from dataclasses import dataclass

__all__ = ["Temperature"]


@dataclass(slots=True)
class Temperature:
    celcius: float
    fahrenheit: float
