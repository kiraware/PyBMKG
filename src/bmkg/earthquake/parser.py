import json
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
    FeltEarthquakeData,
    InfoFeltEarthquakeData,
    InfoLatestEarthquakeData,
    InfoStrongEarthquakeData,
    LatestEarthquakeData,
    StrongEarthquakeData,
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


def parse_latest_earthquake_data(latest_earthquake_data: bytes) -> LatestEarthquake:
    data: InfoLatestEarthquakeData = json.loads(latest_earthquake_data)

    latest_earthquake_data_dict: LatestEarthquakeData = data["Infogempa"]["gempa"]
    earthquake_data = parse_earthquake_data(latest_earthquake_data_dict)
    potensi = latest_earthquake_data_dict["Potensi"]
    dirasakan = latest_earthquake_data_dict["Dirasakan"]
    shakemap = latest_earthquake_data_dict["Shakemap"]

    return LatestEarthquake.from_earthquake_data(
        earthquake_data,
        potensi=potensi,
        dirasakan=dirasakan,
        shakemap=shakemap,
    )


def parse_strong_earthquake_data(
    strong_earthquake_data: bytes,
) -> Iterator[StrongEarthquake]:
    data: InfoStrongEarthquakeData = json.loads(strong_earthquake_data)

    strong_earthquake_data_dict: StrongEarthquakeData
    for strong_earthquake_data_dict in data["Infogempa"]["gempa"]:
        earthquake_data = parse_earthquake_data(strong_earthquake_data_dict)
        potensi = strong_earthquake_data_dict["Potensi"]

        yield StrongEarthquake.from_earthquake_data(
            earthquake_data,
            potensi=potensi,
        )


def parse_felt_earthquake_data(
    felt_earthquake_data: bytes,
) -> Iterator[FeltEarthquake]:
    data: InfoFeltEarthquakeData = json.loads(felt_earthquake_data)

    felt_earthquake_data_dict: FeltEarthquakeData
    for felt_earthquake_data_dict in data["Infogempa"]["gempa"]:
        earthquake_data = parse_earthquake_data(felt_earthquake_data_dict)
        dirasakan = felt_earthquake_data_dict["Dirasakan"]

        yield FeltEarthquake.from_earthquake_data(
            earthquake_data,
            dirasakan=dirasakan,
        )
