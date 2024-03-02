"""
Module to store a str enum class representation cardinal directions.
"""

from enum import StrEnum

__all__ = ["Cardinal"]


class Cardinal(StrEnum):
    """
    A str enum class that define valid cardinal direction.

    Attributes:
        NORTH: `"N"`
        NORTH_NORTHEAST: `"NNE"`
        NORTHEAST: `"NE"`
        EAST_NORTHEAST: `"ENE"`
        EAST: `"E"`
        EAST_SOUTHEAST: `"ESE"`
        SOUTHEAST: `"SE"`
        SOUTH_SOUTHEAST: `"SSE"`
        SOUTH: `"S"`
        SOUTH_SOUTHWEST: `"SSW"`
        SOUTHWEST: `"SW"`
        WEST_SOUTHWEST: `"WSW"`
        WEST: `"W"`
        WEST_NORTHWEST: `"WNW"`
        NORTHWEST: `"NW"`
        NORTH_NORTHWEST: `"NNW"`
        VARIABLE: `"VARIABLE"`

    Examples:
        >>> Cardinal("N")
        <Cardinal.NORTH: 'N'>
        >>> Cardinal["NORTH"]
        <Cardinal.NORTH: 'N'>
        >>> Cardinal.NORTH
        <Cardinal.NORTH: 'N'>
        >>> Cardinal.NORTH == "N"
        True
        >>> print(Cardinal.NORTH)
        N

    Note:
        `VARIABLE` direction mean as its name suggest, the direction can't be
        determined.
    """

    NORTH: str = "N"
    NORTH_NORTHEAST: str = "NNE"
    NORTHEAST: str = "NE"
    EAST_NORTHEAST: str = "ENE"
    EAST: str = "E"
    EAST_SOUTHEAST: str = "ESE"
    SOUTHEAST: str = "SE"
    SOUTH_SOUTHEAST: str = "SSE"
    SOUTH: str = "S"
    SOUTH_SOUTHWEST: str = "SSW"
    SOUTHWEST: str = "SW"
    WEST_SOUTHWEST: str = "WSW"
    WEST: str = "W"
    WEST_NORTHWEST: str = "WNW"
    NORTHWEST: str = "NW"
    NORTH_NORTHWEST: str = "NNW"
    VARIABLE: str = "VARIABLE"
