from dataclasses import dataclass

__all__ = ["Location"]


@dataclass(slots=True)
class Location:
    """
    A schema used to store information about a geographic location.

    Attributes:
        admin_level_1: The administrative level 1 code, typically representing the province.
        admin_level_2: The administrative level 2 code, typically representing the city or district.
        admin_level_3: The administrative level 3 code, typically representing the subdistrict.
        admin_level_4: The administrative level 4 code, typically representing a more localized area (e.g., village or neighborhood).
        province: The name of the province or state.
        city: The name of the city or district.
        subdistrict: The name of the subdistrict (a subdivision of a city or district).
        village: The name of the village or rural area.
        longitude: The geographic longitude coordinate of the location.
        latitude: The geographic latitude coordinate of the location.
        timezone: The time zone identifier for the location, e.g., "Asia/Jakarta".
    """

    admin_level_1: str
    admin_level_2: str
    admin_level_3: str
    admin_level_4: str
    province: str
    city: str
    subdistrict: str
    village: str
    longitude: float
    latitude: float
    timezone: str
