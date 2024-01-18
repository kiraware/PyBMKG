from dataclasses import dataclass

__all__ = ["Name"]


@dataclass(unsafe_hash=True, slots=True)
class Name:
    """
    A schema used to store info about name of an area.

    Attributes:
        en_US: name of an area in english.
        id_ID: name of an area in indonesian.
    """

    en_US: str
    id_ID: str
