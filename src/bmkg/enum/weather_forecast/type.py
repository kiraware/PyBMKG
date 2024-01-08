"""
Module to store an enum class representation area type.
"""
from enum import Enum

__all__ = ["Type"]


class Type(Enum):
    """
    An enum class that define valid area type.

    There are two valid area type:
    `LAND` is `"land"` and `SEA` is `"sea"`.
    """

    LAND = "land"
    SEA = "sea"
