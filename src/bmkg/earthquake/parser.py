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
    EarthquakeDict,
    FeltEarthquakeDict,
    InfoFeltEarthquakeDict,
    InfoLatestEarthquakeDict,
    InfoStrongEarthquakeDict,
    LatestEarthquakeDict,
    StrongEarthquakeDict,
)

__all__ = [
    "parse_earthquake_dict",
    "parse_latest_earthquake_data",
    "parse_strong_earthquake_data",
    "parse_felt_earthquake_data",
]


def parse_earthquake_dict(earthquake_dict: EarthquakeDict) -> Earthquake:
    dt = earthquake_dict["DateTime"]
    coordinate = earthquake_dict["Coordinates"].split(",")
    latitude = coordinate[0]
    longitude = coordinate[1]
    magnitude = earthquake_dict["Magnitude"]
    kedalaman = earthquake_dict["Kedalaman"]
    wilayah = earthquake_dict["Wilayah"]

    return Earthquake(
        datetime.fromisoformat(dt),
        Coordinate(float(latitude), float(longitude)),
        float(magnitude),
        kedalaman,
        wilayah,
    )


def parse_latest_earthquake_data(
    info_latest_earthquake_dict: InfoLatestEarthquakeDict,
) -> LatestEarthquake:
    latest_earthquake_dict: LatestEarthquakeDict = info_latest_earthquake_dict[
        "Infogempa"
    ]["gempa"]
    earthquake = parse_earthquake_dict(latest_earthquake_dict)
    potensi = latest_earthquake_dict["Potensi"]
    dirasakan = latest_earthquake_dict["Dirasakan"]
    shakemap = latest_earthquake_dict["Shakemap"]

    return LatestEarthquake(earthquake, potensi, dirasakan, shakemap)


def parse_strong_earthquake_data(
    info_strong_earthquake_dict: InfoStrongEarthquakeDict,
) -> Iterator[StrongEarthquake]:
    strong_earthquake_dict: StrongEarthquakeDict
    for strong_earthquake_dict in info_strong_earthquake_dict["Infogempa"]["gempa"]:
        earthquake = parse_earthquake_dict(strong_earthquake_dict)
        potensi = strong_earthquake_dict["Potensi"]

        yield StrongEarthquake(earthquake, potensi)


def parse_felt_earthquake_data(
    info_felt_earthquake_dict: InfoFeltEarthquakeDict,
) -> Iterator[FeltEarthquake]:
    felt_earthquake_dict: FeltEarthquakeDict
    for felt_earthquake_dict in info_felt_earthquake_dict["Infogempa"]["gempa"]:
        earthquake = parse_earthquake_dict(felt_earthquake_dict)
        dirasakan = felt_earthquake_dict["Dirasakan"]

        yield FeltEarthquake(earthquake, dirasakan)
