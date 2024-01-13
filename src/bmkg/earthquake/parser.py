from collections.abc import Iterator
from datetime import datetime

from ..common.schemas import Coordinate
from .schemas import (
    Earthquake,
    FeltEarthquake,
    LatestEarthquake,
    StrongEarthquake,
)
from .types import (
    EarthquakeData,
    InfoFeltEarthquakeData,
    InfoLatestEarthquakeData,
    InfoStrongEarthquakeData,
)

__all__ = [
    "parse_earthquake_data",
    "parse_latest_earthquake_data",
    "parse_strong_earthquake_data",
    "parse_felt_earthquake_data",
]


def parse_earthquake_data(earthquake_data: EarthquakeData) -> Earthquake:
    dt = earthquake_data["DateTime"]
    coordinate = earthquake_data["Coordinates"].split(",")
    latitude = coordinate[0]
    longitude = coordinate[1]
    magnitude = earthquake_data["Magnitude"]
    kedalaman = earthquake_data["Kedalaman"]
    wilayah = earthquake_data["Wilayah"]

    return Earthquake(
        datetime.fromisoformat(dt),
        Coordinate(float(latitude), float(longitude)),
        float(magnitude),
        kedalaman,
        wilayah,
    )


def parse_latest_earthquake_data(
    info_latest_earthquake_data: InfoLatestEarthquakeData,
) -> LatestEarthquake:
    latest_earthquake_data = info_latest_earthquake_data["Infogempa"]["gempa"]
    earthquake = parse_earthquake_data(latest_earthquake_data)
    potensi = latest_earthquake_data["Potensi"]
    dirasakan = latest_earthquake_data["Dirasakan"]
    shakemap = latest_earthquake_data["Shakemap"]

    return LatestEarthquake(earthquake, potensi, dirasakan, shakemap)


def parse_strong_earthquake_data(
    info_strong_earthquake_data: InfoStrongEarthquakeData,
) -> Iterator[StrongEarthquake]:
    for strong_earthquake_data in info_strong_earthquake_data["Infogempa"]["gempa"]:
        earthquake = parse_earthquake_data(strong_earthquake_data)
        potensi = strong_earthquake_data["Potensi"]

        yield StrongEarthquake(earthquake, potensi)


def parse_felt_earthquake_data(
    info_felt_earthquake_data: InfoFeltEarthquakeData,
) -> Iterator[FeltEarthquake]:
    for felt_earthquake_data in info_felt_earthquake_data["Infogempa"]["gempa"]:
        earthquake = parse_earthquake_data(felt_earthquake_data)
        dirasakan = felt_earthquake_data["Dirasakan"]

        yield FeltEarthquake(earthquake, dirasakan)
