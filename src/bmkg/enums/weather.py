"""
Module to store an int enum class representation of the weather code.
"""

from enum import IntEnum

__all__ = ["Weather"]


class Weather(IntEnum):
    """
    An int enum class that define valid weather.

    Attributes:
        CLEAR_SKIES (int): `0`
        SUNNY (int): `1`
        PARTLY_CLOUDY (int): `2`
        MOSTLY_CLOUDY (int): `3`
        OVERCAST (int): `4`
        HAZE (int): `5`
        SMOKE (int): `10`
        THUNDER (int): `17`
        FOG (int): `45`
        LIGHT_RAIN (int): `61`
        MODERATE_RAIN (int): `63`
        ISOLATED_SHOWER (int): `80`
        THUNDERSTORM (int): `95`
        SEVERE_THUNDERSTORM (int): `97`

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
    """

    CLEAR_SKIES = 0
    SUNNY = 1
    PARTLY_CLOUDY = 2
    MOSTLY_CLOUDY = 3
    OVERCAST = 4
    HAZE = 5
    SMOKE = 10
    THUNDER = 17
    FOG = 45
    LIGHT_RAIN = 61
    MODERATE_RAIN = 63
    ISOLATED_SHOWER = 80
    THUNDERSTORM = 95
    SEVERE_THUNDERSTORM = 97
