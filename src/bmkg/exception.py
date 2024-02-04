__all__ = [
    "BMKGError",
    "WeatherForecastParseError",
]


class BMKGError(Exception):
    """
    General BMKG API exception.
    """

    pass


class WeatherForecastParseError(BMKGError):
    """
    Weather forecast parse exception.
    """

    pass
