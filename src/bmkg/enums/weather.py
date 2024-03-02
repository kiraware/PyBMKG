"""
Module to store an int enum class representation of the weather code.
"""

from enum import IntEnum

__all__ = ["Weather"]


class Weather(IntEnum):
    """
    An int enum class that define valid weather.

    Attributes:
        CLEAR_SKIES: `0`
        PARTLY_CLOUDY: `1`
        PARTLY_CLOUDY2: `2`
        MOSTLY_CLOUDY: `3`
        OVERCAST: `4`
        HAZE: `5`
        SMOKE: `10`
        FOG: `45`
        LIGHT_RAIN: `60`
        RAIN: `61`
        HEAVY_RAIN: `63`
        ISOLATED_SHOWER: `80`
        SEVERE_THUNDERSTORM: `95`
        SEVERE_THUNDERSTORM2: `97`

    Examples:
        >>> Weather(0)
        <Weather.CLEAR_SKIES: 0>
        >>> Weather["CLEAR_SKIES"]
        <Weather.CLEAR_SKIES: 0>
        >>> Weather.CLEAR_SKIES
        <Weather.CLEAR_SKIES: 0>
        >>> Weather.CLEAR_SKIES == 0
        True
        >>> print(Weather.CLEAR_SKIES)
        0

    Note:
        There is `PARTLY_CLOUDY` and `PARTLY_CLOUDY2`, the weather
        condition is equal only the number representation is different. This is
        also hold true for `SEVERE_THUNDERSTORM` and `SEVERE_THUNDERSTORM2`.
    """

    CLEAR_SKIES: int = 0
    PARTLY_CLOUDY: int = 1
    PARTLY_CLOUDY2: int = 2
    MOSTLY_CLOUDY: int = 3
    OVERCAST: int = 4
    HAZE: int = 5
    SMOKE: int = 10
    FOG: int = 45
    LIGHT_RAIN: int = 60
    RAIN: int = 61
    HEAVY_RAIN: int = 63
    ISOLATED_SHOWER: int = 80
    SEVERE_THUNDERSTORM: int = 95
    SEVERE_THUNDERSTORM2: int = 97
