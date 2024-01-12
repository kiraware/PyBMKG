from typing import TypedDict

__all__ = [
    "Shakemap",
    "EarthquakeData",
    "FeltEarthquakeData",
    "LatestEarthquakeData",
    "StrongEarthquakeData",
    "InfoFeltEarthquakeData",
    "InfoLatestEarthquakeData",
    "InfoStrongEarthquakeData",
]

Shakemap = str


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
    Shakemap: Shakemap


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
