from dataclasses import dataclass

from ..types import Shakemap
from .earthquake_data import EarthquakeData

__all__ = ["LatestEarthquakeData"]


@dataclass(slots=True)
class LatestEarthquakeData(EarthquakeData):
    potensi: str
    dirasakan: str
    shakemap: Shakemap
