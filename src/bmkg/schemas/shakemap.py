from dataclasses import dataclass

__all__ = ["Shakemap"]


@dataclass(slots=True)
class Shakemap:
    """
    A schema used to store info about shakemap.

    Attributes:
        file_name: name of shakemap file.
    """

    file_name: str
