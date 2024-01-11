import json
from collections.abc import Iterator
from datetime import datetime

from ..common.schemas import Coordinate
from .schemas import (
    EarthquakeData,
    FeltEarthquakeData,
    LatestEarthquakeData,
    StrongEarthquakeData,
)
from .types import (
    EarthquakeDataDict,
    FeltEarthquakeDataDict,
    InfoFeltEarthquakeDataDict,
    InfoLatestEarthquakeDataDict,
    InfoStrongEarthquakeDataDict,
    LatestEarthquakeDataDict,
    StrongEarthquakeDataDict,
)

__all__ = [
    "parse_earthquake_data",
    "parse_latest_earthquake_data",
    "parse_strong_earthquake_data",
    "parse_felt_earthquake_data",
]


def parse_earthquake_data(earthquake_data: EarthquakeDataDict) -> EarthquakeData:
    dt = earthquake_data["DateTime"]
    coordinate = earthquake_data["Coordinates"].split(",")
    latitude = coordinate[0]
    longitude = coordinate[1]
    magnitude = earthquake_data["Magnitude"]
    kedalaman = earthquake_data["Kedalaman"]
    wilayah = earthquake_data["Wilayah"]

    return EarthquakeData(
        datetime.fromisoformat(dt),
        Coordinate(float(latitude), float(longitude)),
        float(magnitude),
        kedalaman,
        wilayah,
    )


def parse_latest_earthquake_data(latest_earthquake_data: bytes) -> LatestEarthquakeData:
    data: InfoLatestEarthquakeDataDict = json.loads(latest_earthquake_data)

    latest_earthquake_data_dict: LatestEarthquakeDataDict = data["Infogempa"]["gempa"]
    earthquake_data = parse_earthquake_data(latest_earthquake_data_dict)
    potensi = latest_earthquake_data_dict["Potensi"]
    dirasakan = latest_earthquake_data_dict["Dirasakan"]
    shakemap = latest_earthquake_data_dict["Shakemap"]

    return LatestEarthquakeData.from_earthquake_data(
        earthquake_data,
        potensi=potensi,
        dirasakan=dirasakan,
        shakemap=shakemap,
    )


def parse_strong_earthquake_data(
    strong_earthquake_data: bytes,
) -> Iterator[StrongEarthquakeData]:
    data: InfoStrongEarthquakeDataDict = json.loads(strong_earthquake_data)

    strong_earthquake_data_dict: StrongEarthquakeDataDict
    for strong_earthquake_data_dict in data["Infogempa"]["gempa"]:
        earthquake_data = parse_earthquake_data(strong_earthquake_data_dict)
        potensi = strong_earthquake_data_dict["Potensi"]

        yield StrongEarthquakeData.from_earthquake_data(
            earthquake_data,
            potensi=potensi,
        )


def parse_felt_earthquake_data(
    felt_earthquake_data: bytes,
) -> Iterator[FeltEarthquakeData]:
    data: InfoFeltEarthquakeDataDict = json.loads(felt_earthquake_data)

    felt_earthquake_data_dict: FeltEarthquakeDataDict
    for felt_earthquake_data_dict in data["Infogempa"]["gempa"]:
        earthquake_data = parse_earthquake_data(felt_earthquake_data_dict)
        dirasakan = felt_earthquake_data_dict["Dirasakan"]

        yield FeltEarthquakeData.from_earthquake_data(
            earthquake_data,
            dirasakan=dirasakan,
        )
