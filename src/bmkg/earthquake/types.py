from typing import TypedDict

__all__ = [
    "Shakemap",
    "EarthquakeDict",
    "FeltEarthquakeDict",
    "LatestEarthquakeDict",
    "StrongEarthquakeDict",
    "InfoFeltEarthquakeDict",
    "InfoLatestEarthquakeDict",
    "InfoStrongEarthquakeDict",
]

Shakemap = str


class EarthquakeDict(TypedDict):
    Tanggal: str
    Jam: str
    DateTime: str
    Coordinates: str
    Lintang: str
    Bujur: str
    Magnitude: str
    Kedalaman: str
    Wilayah: str


class StrongEarthquakeDict(EarthquakeDict):
    Potensi: str


class FeltEarthquakeDict(EarthquakeDict):
    Dirasakan: str


class LatestEarthquakeDict(EarthquakeDict):
    Potensi: str
    Dirasakan: str
    Shakemap: Shakemap


class _StrongEarthquakeDict(TypedDict):
    gempa: list[StrongEarthquakeDict]


class InfoStrongEarthquakeDict(TypedDict):
    Infogempa: _StrongEarthquakeDict


class _FeltEarthquakeDict(TypedDict):
    gempa: list[FeltEarthquakeDict]


class InfoFeltEarthquakeDict(TypedDict):
    Infogempa: _FeltEarthquakeDict


class _LatestEarthquakeDict(TypedDict):
    gempa: LatestEarthquakeDict


class InfoLatestEarthquakeDict(TypedDict):
    Infogempa: _LatestEarthquakeDict
