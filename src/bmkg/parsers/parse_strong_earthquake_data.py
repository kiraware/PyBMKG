from collections.abc import Iterator

from ..schemas import StrongEarthquake
from ..types import InfoStrongEarthquakeData
from .parse_earthquake_data import parse_earthquake_data

__all__ = ["parse_strong_earthquake_data"]


def parse_strong_earthquake_data(
    info_strong_earthquake_data: InfoStrongEarthquakeData,
) -> Iterator[StrongEarthquake]:
    """
    Parse `InfoStrongEarthquakeData` JSON.

    Args:
        info_strong_earthquake_data: A dict representing JSON of info strong earthquake.

    Yields:
        A `StrongEarthquake` schema.

    Examples:
        >>> info_strong_earthquake_data = InfoStrongEarthquakeData(
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
    """

    for strong_earthquake_data in info_strong_earthquake_data["Infogempa"]["gempa"]:
        earthquake = parse_earthquake_data(strong_earthquake_data)
        potency = strong_earthquake_data["Potensi"]

        yield StrongEarthquake(earthquake, potency)
