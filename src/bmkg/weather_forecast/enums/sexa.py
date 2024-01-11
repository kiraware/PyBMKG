"""
Module to store an enum class representation sexa directions.
"""
from enum import Enum

__all__ = ["Sexa"]


class Sexa(Enum):
    """
    An enum class that define valid sexa direction.

    There are sixteen valid sexa direction:
    `NORTH_NORTHEAST` is `"2230"`, `NORTHEAST` is `"4500"`,
    `EAST_NORTHEAST` is `"6730"`, `EAST` is `"9000"`,
    `EAST_SOUTHEAST` is `"11230"`, `SOUTHEAST` is `"13500"`,
    `SOUTH_SOUTHEAST` is `"15730"`, `SOUTH` is `"18000"`,
    `SOUTH_SOUTHWEST` is `"20230"`, `SOUTHWEST` is `"22500"`,
    `WEST_SOUTHWEST` is `"24730"`, `WEST` is `"27000"`,
    `WEST_NORTHWEST` is `"29230"`, `NORTHWEST` is `"31500"`,
    `NORTH_NORTHWEST` is `"33730"`, `VARIABLE` is `"000"`

    `VARIABLE` direction mean as it's name suggest, the direction can't be
    determined. Notice there is no `NORTH` due to bug in BMKG API.
    """

    # FIXME
    # Change NORTH or VARIABLE if the bug was fixed
    # Possible bug in BMKG API that NORTH equal to VARIABLE
    # NORTH = "000"
    NORTH_NORTHEAST = "2230"
    NORTHEAST = "4500"
    EAST_NORTHEAST = "6730"
    EAST = "9000"
    EAST_SOUTHEAST = "11230"
    SOUTHEAST = "13500"
    SOUTH_SOUTHEAST = "15730"
    SOUTH = "18000"
    SOUTH_SOUTHWEST = "20230"
    SOUTHWEST = "22500"
    WEST_SOUTHWEST = "24730"
    WEST = "27000"
    WEST_NORTHWEST = "29230"
    NORTHWEST = "31500"
    NORTH_NORTHWEST = "33730"
    VARIABLE = "000"
