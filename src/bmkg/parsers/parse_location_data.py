from ..schemas import Location
from ..types import LocationData

__all__ = ["parse_location_data"]


def parse_location_data(location_data: LocationData) -> Location:
    """
    Parse `LocationData` JSON.

    Args:
        location_data: A dict representing JSON of weather forecast data.

    Returns:
        A `Location` schema.
    """

    return Location(
        location_data["adm1"],
        location_data["adm2"],
        location_data["adm3"],
        location_data["adm4"],
        location_data["provinsi"],
        location_data["kotkab"],
        location_data["kecamatan"],
        location_data["desa"],
        float(location_data["lon"]),
        float(location_data["lat"]),
        location_data["timezone"],
    )
