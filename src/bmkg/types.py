from datetime import datetime
from typing import Iterator, Literal, TypedDict

from .enums import Weather
from .schemas import (
    Humidity,
    Temperature,
    WindDirection,
    WindSpeed,
)

__all__ = [
    "WeatherForecastParameter",
    "WeatherForecastParameterId",
    "WeatherForecastParameters",
    "EarthquakeData",
    "FeltEarthquakeData",
    "LatestEarthquakeData",
    "StrongEarthquakeData",
    "InfoFeltEarthquakeData",
    "InfoLatestEarthquakeData",
    "InfoStrongEarthquakeData",
]


class WeatherForecastParameters(TypedDict, total=False):
    datetime: Iterator[datetime]
    hu: Iterator[Humidity]
    humax: Iterator[Humidity]
    humin: Iterator[Humidity]
    t: Iterator[Temperature]
    tmax: Iterator[Temperature]
    tmin: Iterator[Temperature]
    weather: Iterator[Weather]
    wd: Iterator[WindDirection]
    ws: Iterator[WindSpeed]


WeatherForecastParameter = (
    Iterator[datetime]
    | Iterator[Humidity]
    | Iterator[Temperature]
    | Iterator[Weather]
    | Iterator[WindDirection]
    | Iterator[WindSpeed]
)

WeatherForecastParameterId = Literal[
    "datetime", "hu", "humax", "humin", "t", "tmax", "tmin", "weather", "wd", "ws"
]


class EarthquakeData(TypedDict):
    Tanggal: str
    Jam: str
    DateTime: str
    Coordinates: str
    Lintang: str
    Bujur: str
    Magnitude: str
    Kedalaman: str
    Wilayah: str


class StrongEarthquakeData(EarthquakeData):
    Potensi: str


class FeltEarthquakeData(EarthquakeData):
    Dirasakan: str


class LatestEarthquakeData(EarthquakeData):
    Potensi: str
    Dirasakan: str
    Shakemap: str


class _StrongEarthquakeData(TypedDict):
    gempa: list[StrongEarthquakeData]


class InfoStrongEarthquakeData(TypedDict):
    Infogempa: _StrongEarthquakeData


class _FeltEarthquakeData(TypedDict):
    gempa: list[FeltEarthquakeData]


class InfoFeltEarthquakeData(TypedDict):
    Infogempa: _FeltEarthquakeData


class _LatestEarthquakeData(TypedDict):
    gempa: LatestEarthquakeData


class InfoLatestEarthquakeData(TypedDict):
    Infogempa: _LatestEarthquakeData
