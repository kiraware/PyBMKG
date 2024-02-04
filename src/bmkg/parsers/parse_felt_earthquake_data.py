from collections.abc import Iterator

from ..schemas import FeltEarthquake
from ..types import InfoFeltEarthquakeData
from .parse_earthquake_data import parse_earthquake_data

__all__ = ["parse_felt_earthquake_data"]


def parse_felt_earthquake_data(
    info_felt_earthquake_data: InfoFeltEarthquakeData,
) -> Iterator[FeltEarthquake]:
    """
    Parse `InfoFeltEarthquakeData` JSON.

    Args:
        info_felt_earthquake_data: A dict representing JSON of info felt earthquake.

    Yields:
        A `FeltEarthquake` schema.

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
    """

    for felt_earthquake_data in info_felt_earthquake_data["Infogempa"]["gempa"]:
        earthquake = parse_earthquake_data(felt_earthquake_data)
        felt = felt_earthquake_data["Dirasakan"]

        yield FeltEarthquake(earthquake, felt)
