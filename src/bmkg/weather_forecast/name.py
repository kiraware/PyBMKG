from dataclasses import dataclass

__all__ = ["Name"]


@dataclass(unsafe_hash=True, slots=True)
class Name:
    en_US: str
    id_ID: str
