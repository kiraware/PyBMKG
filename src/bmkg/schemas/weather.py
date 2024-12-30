import datetime as dt
from dataclasses import dataclass

from .. import enums

__all__ = ["Weather"]


@dataclass(slots=True)
class Weather:
    """
    A schema used to store information about a weather.

    Attributes:
        datetime: The datetime of the weather data in UTC format.
        t: Temperature in degrees Celsius.
        tcc: Total cloud cover percentage (0-100%).
        tp: Precipitation amount in millimeters.
        weather: Weather condition code, corresponds to a predefined set of weather conditions.
        wd_deg: Wind direction in degrees (0-360), where 0° is North.
        wd: Wind direction from which the wind blows.
        wd_to: Wind direction the wind is blowing towards.
        ws: Wind speed in kilometers per hour (km/h).
        hu: Humidity percentage (0-100%).
        vs: Visibility in meters.
        time_index: Time index in the format `"x-y"`, where `x` is the hour start of the forecast, and `y` is the hour end of the forecast.
        analysis_date: The date when the weather data was generated (in UTC format).
        image: URL to an image representing the weather condition (e.g., an icon).
        utc_datetime: The UTC datetime when the weather data was recorded.
        local_datetime: The local datetime when the weather data was recorded.
    """

    datetime: dt.datetime
    t: int
    tcc: int
    tp: float
    weather: enums.Weather
    wd_deg: int
    wd: enums.Cardinal
    wd_to: enums.Cardinal
    ws: float
    hu: int
    vs: int
    time_index: str
    analysis_date: dt.datetime
    image: str
    utc_datetime: dt.datetime
    local_datetime: dt.datetime
