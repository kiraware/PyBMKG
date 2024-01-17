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
    """
    Parse `EarthquakeData` JSON.

    Examples:
        >>> earthquake_data = EarthquakeData(
        ...     {
        ...         "Tanggal": "14 Jan 2024",
        ...         "Jam": "03:13:37 WIB",
        ...         "DateTime": "2024-01-13T20:13:37+00:00",
        ...         "Coordinates": "-6.75,106.55",
        ...         "Lintang": "6.75 LS",
        ...         "Bujur": "106.55 BT",
        ...         "Magnitude": "3.5",
        ...         "Kedalaman": "5 km",
        ...         "Wilayah": "Pusat gempa berada di darat 26 km Utara Kab Sukabumi",
        ...     }
        ... )
        >>> parse_earthquake_data(earthquake_data)
        Earthquake(datetime=datetime.datetime(2024, 1, 13, 20, 13, 37, tzinfo=datetim...

    Args:
        earthquake_data: A dict representing JSON of earthquake.

    Returns:
        An `Earthquake` schema.
    """

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
    """
    Parse `InfoLatestEarthquakeData` JSON.

    Examples:
        >>> info_latest_earthquake_data = InfoLatestEarthquakeData(
        ...     {
        ...         "Infogempa": {
        ...             "gempa": {
        ...                 "Tanggal": "15 Jan 2024",
        ...                 "Jam": "16:07:08 WIB",
        ...                 "DateTime": "2024-01-15T09:07:08+00:00",
        ...                 "Coordinates": "-3.98,122.45",
        ...                 "Lintang": "3.98 LS",
        ...                 "Bujur": "122.45 BT",
        ...                 "Magnitude": "2.6",
        ...                 "Kedalaman": "9 km",
        ...                 "Wilayah": "Pusat gempa berada di darat 2,5 km BaratDaya P",
        ...                 "Potensi": "Gempa ini dirasakan untuk diteruskan pada masy",
        ...                 "Dirasakan": "II Kendari",
        ...                 "Shakemap": "20240115160708.mmi.jpg",
        ...             }
        ...         }
        ...     }
        ... )
        >>> parse_latest_earthquake_data(info_latest_earthquake_data)
        LatestEarthquake(earthquake=Earthquake(datetime=datetime.datetime(2024, 1, 15...

    Args:
        info_latest_earthquake_data: A dict representing JSON of info latest earthquake.

    Returns:
        An `LatestEarthquake` schema.
    """

    latest_earthquake_data = info_latest_earthquake_data["Infogempa"]["gempa"]
    earthquake = parse_earthquake_data(latest_earthquake_data)
    potensi = latest_earthquake_data["Potensi"]
    dirasakan = latest_earthquake_data["Dirasakan"]
    shakemap = latest_earthquake_data["Shakemap"]

    return LatestEarthquake(earthquake, potensi, dirasakan, shakemap)


def parse_strong_earthquake_data(
    info_strong_earthquake_data: InfoStrongEarthquakeData,
) -> Iterator[StrongEarthquake]:
    """
    Parse `InfoStrongEarthquakeData` JSON.

    Examples:
        >>> info_strong_earthquake_data = InfoLatestEarthquakeData(
        ...     {
        ...         "Infogempa": {
        ...             "gempa": [
        ...                 {
        ...                     "Tanggal": "09 Jan 2024",
        ...                     "Jam": "12:25:24 WIB",
        ...                     "DateTime": "2024-01-09T05:25:24+00:00",
        ...                     "Coordinates": "-4.46,133.91",
        ...                     "Lintang": "4.46 LS",
        ...                     "Bujur": "133.91 BT",
        ...                     "Magnitude": "5.3",
        ...                     "Kedalaman": "10 km",
        ...                     "Wilayah": "130 km BaratDaya KAIMANA-PAPUABRT",
        ...                     "Potensi": "Tidak berpotensi tsunami",
        ...                 }
        ...             ]
        ...         }
        ...     }
        ... )
        >>> parse_strong_earthquake_data(info_strong_earthquake_data)
        <generator object parse_strong_earthquake_data at ...>

    Args:
        info_strong_earthquake_data: A dict representing JSON of info strong earthquake.

    Returns:
        An iterator of `StrongEarthquake` schema.
    """

    for strong_earthquake_data in info_strong_earthquake_data["Infogempa"]["gempa"]:
        earthquake = parse_earthquake_data(strong_earthquake_data)
        potensi = strong_earthquake_data["Potensi"]

        yield StrongEarthquake(earthquake, potensi)


def parse_felt_earthquake_data(
    info_felt_earthquake_data: InfoFeltEarthquakeData,
) -> Iterator[FeltEarthquake]:
    """
    Parse `InfoFeltEarthquakeData` JSON.

    Examples:
        >>> info_felt_earthquake_data = InfoFeltEarthquakeData(
        ...     {
        ...         "Infogempa": {
        ...             "gempa": [
        ...                 {
        ...                     "Tanggal": "15 Jan 2024",
        ...                     "Jam": "16:07:08 WIB",
        ...                     "DateTime": "2024-01-15T09:07:08+00:00",
        ...                     "Coordinates": "-3.98,122.45",
        ...                     "Lintang": "3.98 LS",
        ...                     "Bujur": "122.45 BT",
        ...                     "Magnitude": "2.6",
        ...                     "Kedalaman": "9 km",
        ...                     "Wilayah": "Pusat gempa berada di darat 2,5 km BaratDa",
        ...                     "Dirasakan": "II Kendari",
        ...                 }
        ...             ]
        ...         }
        ...     }
        ... )
        >>> parse_felt_earthquake_data(info_felt_earthquake_data)
        <generator object parse_felt_earthquake_data at ...>

    Args:
        info_felt_earthquake_data: A dict representing JSON of info felt earthquake.

    Returns:
        An iterator of `FeltEarthquake` schema.
    """

    for felt_earthquake_data in info_felt_earthquake_data["Infogempa"]["gempa"]:
        earthquake = parse_earthquake_data(felt_earthquake_data)
        dirasakan = felt_earthquake_data["Dirasakan"]

        yield FeltEarthquake(earthquake, dirasakan)
