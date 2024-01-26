"""
Module to store a str enum class representation area type.
"""
from enum import StrEnum

__all__ = ["Type"]


class Type(StrEnum):
    """
    A str enum class that define valid area type.

    Attributes:
        LAND: `"land"`
        SEA: `"sea"`

    Examples:
        >>> Type("land")
        <Type.LAND: 'land'>
        >>> Type["LAND"]
        <Type.LAND: 'land'>
        >>> Type.LAND
        <Type.LAND: 'land'>
        >>> Type.LAND == "land"
        True
        >>> print(Type.LAND)
        land
    """

    LAND: str = "land"
    SEA: str = "sea"
