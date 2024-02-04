from ..schemas import LatestEarthquake, Shakemap
from ..types import InfoLatestEarthquakeData
from .parse_earthquake_data import parse_earthquake_data

__all__ = ["parse_latest_earthquake_data"]


def parse_latest_earthquake_data(
    info_latest_earthquake_data: InfoLatestEarthquakeData,
) -> LatestEarthquake:
    """
    Parse `InfoLatestEarthquakeData` JSON.

    Args:
        info_latest_earthquake_data: A dict representing JSON of info latest earthquake.

    Returns:
        A `LatestEarthquake` schema.

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
    """

    latest_earthquake_data = info_latest_earthquake_data["Infogempa"]["gempa"]
    earthquake = parse_earthquake_data(latest_earthquake_data)
    potency = latest_earthquake_data["Potensi"]
    felt = latest_earthquake_data["Dirasakan"]
    shakemap = latest_earthquake_data["Shakemap"]

    return LatestEarthquake(earthquake, potency, felt, Shakemap(shakemap))
