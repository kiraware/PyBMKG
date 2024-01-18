"""
Module to store an enum class representation area type.
"""
from enum import Enum

__all__ = ["Type"]


class Type(Enum):
    """
    An enum class that define valid area type.

    Attributes:
        LAND: "land"
        SEA: "sea"
    """

    LAND: str = "land"
    SEA: str = "sea"
