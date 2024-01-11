"""
Module to store an enum class representation of the weather code.
"""
from enum import Enum

__all__ = ["Weather"]


class Weather(Enum):
    """
    An enum class that define valid weather.

    There are fourteen valid weather condition:
    `CLEAR_SKIES` is `0`, `PARTLY_CLOUDY` is `1`, `PARTLY_CLOUDY2` is `2`,
    `MOSTLY_CLOUDY` is `3`, `OVERCAST` is `4`, `HAZE` is `5`, `SMOKE` is `10`,
    `FOG` is `45`, `LIGHT_RAIN` is `60`, `RAIN` is `61`, `HEAVY_RAIN` is `63`,
    `ISOLATED_SHOWER` is `80`, `SEVERE_THUNDERSTORM` is `95`,
    `SEVERE_THUNDERSTORM2` is `97`

    Notice there is `PARTLY_CLOUDY` and `PARTLY_CLOUDY2`, the weather
    condition is equal only the number representation is different. This is
    also hold true for `SEVERE_THUNDERSTORM` and `SEVERE_THUNDERSTORM2`.
    """

    CLEAR_SKIES = 0
    PARTLY_CLOUDY = 1
    PARTLY_CLOUDY2 = 2
    MOSTLY_CLOUDY = 3
    OVERCAST = 4
    HAZE = 5
    SMOKE = 10
    FOG = 45
    LIGHT_RAIN = 60
    RAIN = 61
    HEAVY_RAIN = 63
    ISOLATED_SHOWER = 80
    SEVERE_THUNDERSTORM = 95
    SEVERE_THUNDERSTORM2 = 97
