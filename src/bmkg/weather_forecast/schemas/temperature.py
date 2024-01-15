from dataclasses import dataclass, field

__all__ = ["Temperature"]


@dataclass(slots=True)
class Temperature:
    """
    `Temperature` schema used to store info about temperature in `celcius` and
    `fahrenheit`.

    `celcius` has metadata unit `"C"` and `fahrenheit` has metadata unit
    `"F"`.
    """

    celcius: float = field(metadata={"unit": "C"})
    fahrenheit: float = field(metadata={"unit": "F"})
