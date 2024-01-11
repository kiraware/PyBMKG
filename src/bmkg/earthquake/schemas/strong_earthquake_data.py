from dataclasses import dataclass

from .earthquake_data import EarthquakeData

__all__ = ["StrongEarthquakeData"]


@dataclass(slots=True)
class StrongEarthquakeData(EarthquakeData):
    potensi: str
