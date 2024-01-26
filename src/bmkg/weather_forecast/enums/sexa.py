"""
Module to store a str enum class representation sexa directions.
"""
from enum import StrEnum

__all__ = ["Sexa"]


class Sexa(StrEnum):
    """
    A str enum class that define valid sexa direction.

    Attributes:
        NORTH_NORTHEAST: `"2230"`
        NORTHEAST: `"4500"`
        EAST_NORTHEAST: `"6730"`
        EAST: `"9000"`
        EAST_SOUTHEAST: `"11230"`
        SOUTHEAST: `"13500"`
        SOUTH_SOUTHEAST: `"15730"`
        SOUTH: `"18000"`
        SOUTH_SOUTHWEST: `"20230"`
        SOUTHWEST: `"22500"`
        WEST_SOUTHWEST: `"24730"`
        WEST: `"27000"`
        WEST_NORTHWEST: `"29230"`
        NORTHWEST: `"31500"`
        NORTH_NORTHWEST: `"33730"`
        VARIABLE: `"000"`

    Examples:
        >>> Sexa("2230")
        <Sexa.NORTH_NORTHEAST: '2230'>
        >>> Sexa["NORTH_NORTHEAST"]
        <Sexa.NORTH_NORTHEAST: '2230'>
        >>> Sexa.NORTH_NORTHEAST
        <Sexa.NORTH_NORTHEAST: '2230'>
        >>> Sexa.NORTH_NORTHEAST == "2230"
        True
        >>> print(Sexa.NORTH_NORTHEAST)
        2230

    Note:
        `VARIABLE` direction mean as it's name suggest, the direction can't be
        determined.

    Warning:
        There is no `NORTH` due to bug in BMKG API.
    """

    # FIXME
    # Change NORTH or VARIABLE if the bug was fixed
    # Possible bug in BMKG API that NORTH equal to VARIABLE
    # NORTH: str = "000"
    NORTH_NORTHEAST: str = "2230"
    NORTHEAST: str = "4500"
    EAST_NORTHEAST: str = "6730"
    EAST: str = "9000"
    EAST_SOUTHEAST: str = "11230"
    SOUTHEAST: str = "13500"
    SOUTH_SOUTHEAST: str = "15730"
    SOUTH: str = "18000"
    SOUTH_SOUTHWEST: str = "20230"
    SOUTHWEST: str = "22500"
    WEST_SOUTHWEST: str = "24730"
    WEST: str = "27000"
    WEST_NORTHWEST: str = "29230"
    NORTHWEST: str = "31500"
    NORTH_NORTHWEST: str = "33730"
    VARIABLE: str = "000"
