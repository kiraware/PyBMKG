from dataclasses import dataclass

from .earthquake_data import EarthquakeData

__all__ = ["FeltEarthquakeData"]


@dataclass(slots=True)
class FeltEarthquakeData(EarthquakeData):
    dirasakan: str
