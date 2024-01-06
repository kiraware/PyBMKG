"""
Module to store an enum class representation cardinal directions.
"""
from enum import Enum

__all__ = ["Cardinal"]


class Cardinal(Enum):
    """
    An enum class that define valid cardinal direction.

    There are seventeen valid cardinal directions:
    `NORTH` is `"N"`, `NORTH_NORTHEAST` is `"NNE"`, `NORTHEAST` is `"NE"`,
    `EAST_NORTHEAST` is `"ENE"`, `EAST` is `"E"`, `EAST_SOUTHEAST` is `"ESE"`,
    `SOUTHEAST` is `"SE"`, `SOUTH_SOUTHEAST` is `"SSE"`, `SOUTH` is `"S"`,
    `SOUTH_SOUTHWEST` is `"SSW"`, `SOUTHWEST` is `"SW"`,
    `WEST_SOUTHWEST` is `"WSW"`, `WEST` is `"W"`, `WEST_NORTHWEST` is `"WNW"`,
    `NORTHWEST` is `"NW"`, `NORTH_NORTHWEST` is `"NNW"`,
    `VARIABLE` is `"VARIABLE"`

    `VARIABLE` direction mean as it's name suggest, the direction can't be
    determined.
    """

    NORTH = "N"
    NORTH_NORTHEAST = "NNE"
    NORTHEAST = "NE"
    EAST_NORTHEAST = "ENE"
    EAST = "E"
    EAST_SOUTHEAST = "ESE"
    SOUTHEAST = "SE"
    SOUTH_SOUTHEAST = "SSE"
    SOUTH = "S"
    SOUTH_SOUTHWEST = "SSW"
    SOUTHWEST = "SW"
    WEST_SOUTHWEST = "WSW"
    WEST = "W"
    WEST_NORTHWEST = "WNW"
    NORTHWEST = "NW"
    NORTH_NORTHWEST = "NNW"
    VARIABLE = "VARIABLE"
