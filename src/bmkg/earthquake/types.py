from typing import TypedDict

__all__ = [
    "Shakemap",
    "EarthquakeDataDict",
    "FeltEarthquakeDataDict",
    "LatestEarthquakeDataDict",
    "StrongEarthquakeDataDict",
    "InfoFeltEarthquakeDataDict",
    "InfoLatestEarthquakeDataDict",
    "InfoStrongEarthquakeDataDict",
]

Shakemap = str


class EarthquakeDataDict(TypedDict):
    Tanggal: str
    Jam: str
    DateTime: str
    Coordinates: str
    Lintang: str
    Bujur: str
    Magnitude: str
    Kedalaman: str
    Wilayah: str


class StrongEarthquakeDataDict(EarthquakeDataDict):
    Potensi: str


class FeltEarthquakeDataDict(EarthquakeDataDict):
    Dirasakan: str


class LatestEarthquakeDataDict(EarthquakeDataDict):
    Potensi: str
    Dirasakan: str
    Shakemap: Shakemap


class _StrongEarthquakeDataDict(TypedDict):
    gempa: list[StrongEarthquakeDataDict]


class InfoStrongEarthquakeDataDict(TypedDict):
    Infogempa: _StrongEarthquakeDataDict


class _FeltEarthquakeDataDict(TypedDict):
    gempa: list[FeltEarthquakeDataDict]


class InfoFeltEarthquakeDataDict(TypedDict):
    Infogempa: _FeltEarthquakeDataDict


class _LatestEarthquakeDataDict(TypedDict):
    gempa: LatestEarthquakeDataDict


class InfoLatestEarthquakeDataDict(TypedDict):
    Infogempa: _LatestEarthquakeDataDict
