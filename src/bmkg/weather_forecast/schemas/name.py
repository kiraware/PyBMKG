from dataclasses import dataclass

__all__ = ["Name"]


@dataclass(unsafe_hash=True, slots=True)
class Name:
    """
    `Name` schema used to store info about name of an `Area` either in `en_US` and
    `id_ID`.
    """

    en_US: str
    id_ID: str
