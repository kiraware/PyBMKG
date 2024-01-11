from dataclasses import dataclass, field

__all__ = ["Humidity"]


@dataclass(slots=True)
class Humidity:
    percentage: int = field(metadata={"unit": "%"})
