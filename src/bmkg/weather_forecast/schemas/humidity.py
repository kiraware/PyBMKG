from dataclasses import dataclass, field

__all__ = ["Humidity"]


@dataclass(slots=True)
class Humidity:
    """
    `Humidity` schema used to store info about humidity `percentage`.
    """

    percentage: int = field(metadata={"unit": "%"})
