from datetime import datetime

from ..schemas import (
    Coordinate,
    Earthquake,
)
from ..types import EarthquakeData

__all__ = ["parse_earthquake_data"]


def parse_earthquake_data(earthquake_data: EarthquakeData) -> Earthquake:
    """
    Parse `EarthquakeData` JSON.

    Args:
        earthquake_data: A dict representing JSON of earthquake.

    Returns:
        An `Earthquake` schema.

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
    """

    dt = earthquake_data["DateTime"]
    coordinate = earthquake_data["Coordinates"].split(",")
    latitude = coordinate[0]
    longitude = coordinate[1]
    magnitude = earthquake_data["Magnitude"]
    depth = earthquake_data["Kedalaman"].split()[0]
    region = earthquake_data["Wilayah"]

    return Earthquake(
        datetime.fromisoformat(dt),
        Coordinate(float(latitude), float(longitude)),
        float(magnitude),
        float(depth),
        region,
    )
