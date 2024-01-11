from dataclasses import dataclass, field

__all__ = ["Temperature"]


@dataclass(slots=True)
class Temperature:
    celcius: float = field(metadata={"unit": "C"})
    fahrenheit: float = field(metadata={"unit": "F"})
