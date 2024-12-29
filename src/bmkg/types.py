from typing import TypedDict

__all__ = [
    "EarthquakeData",
    "FeltEarthquakeData",
    "LatestEarthquakeData",
    "StrongEarthquakeData",
    "InfoFeltEarthquakeData",
    "InfoLatestEarthquakeData",
    "InfoStrongEarthquakeData",
    "LocationData",
    "OptionalLocationData",
    "WeatherData",
    "WeatherForecastData",
]


class EarthquakeData(TypedDict):
    Tanggal: str
    Jam: str
    DateTime: str
    Coordinates: str
    Lintang: str
    Bujur: str
    Magnitude: str
    Kedalaman: str
    Wilayah: str


class StrongEarthquakeData(EarthquakeData):
    Potensi: str


class FeltEarthquakeData(EarthquakeData):
    Dirasakan: str


class LatestEarthquakeData(EarthquakeData):
    Potensi: str
    Dirasakan: str
    Shakemap: str


class _StrongEarthquakeData(TypedDict):
    gempa: list[StrongEarthquakeData]


class InfoStrongEarthquakeData(TypedDict):
    Infogempa: _StrongEarthquakeData


class _FeltEarthquakeData(TypedDict):
    gempa: list[FeltEarthquakeData]


class InfoFeltEarthquakeData(TypedDict):
    Infogempa: _FeltEarthquakeData


class _LatestEarthquakeData(TypedDict):
    gempa: LatestEarthquakeData


class InfoLatestEarthquakeData(TypedDict):
    Infogempa: _LatestEarthquakeData


class LocationData(TypedDict):
    adm1: str
    adm2: str
    adm3: str
    adm4: str
    provinsi: str
    kotkab: str
    kecamatan: str
    desa: str
    lon: float
    lat: float
    timezone: str


class OptionalLocationData(LocationData):
    type: str


class WeatherData(TypedDict):
    datetime: str
    t: int
    tcc: int
    tp: float
    weather: int
    weather_desc: str
    weather_desc_en: str
    wd_deg: int
    wd: str
    wd_to: str
    ws: float
    hu: int
    vs: int
    vs_text: str
    time_index: str
    analysis_date: str
    image: str
    utc_datetime: str
    local_datetime: str


class _WeatherForecastData(TypedDict):
    lokasi: OptionalLocationData
    cuaca: list[list[WeatherData]]


class WeatherForecastData(TypedDict):
    lokasi: LocationData
    data: list[_WeatherForecastData]
