from dataclasses import dataclass, field

__all__ = ["Temperature"]


@dataclass(slots=True)
class Temperature:
    """
    A schema used to store info about temperature.

    Attributes:
        celcius: temperature in celcius with C as its unit.
        fahrenheit: temperature in fahrenheit with F as its unit.
    """

    celcius: float = field(metadata={"unit": "C"})
    fahrenheit: float = field(metadata={"unit": "F"})
