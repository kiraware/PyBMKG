from itertools import chain, repeat

import pytest

from bmkg.enum.weather_forecast import Cardinal, Province, Sexa, Type, Weather

expected_cardinal_values = (
    "N",
    "NNE",
    "NE",
    "ENE",
    "E",
    "ESE",
    "SE",
    "SSE",
    "S",
    "SSW",
    "SW",
    "WSW",
    "W",
    "WNW",
    "NW",
    "NNW",
    "VARIABLE",
)
expected_province_values = (
    "Aceh",
    "Bali",
    "BangkaBelitung",
    "Banten",
    "Bengkulu",
    "DIYogyakarta",
    "DKIJakarta",
    "Gorontalo",
    "Jambi",
    "JawaBarat",
    "JawaTengah",
    "JawaTimur",
    "KalimantanBarat",
    "KalimantanSelatan",
    "KalimantanTengah",
    "KalimantanTimur",
    "KalimantanUtara",
    "KepulauanRiau",
    "Lampung",
    "Maluku",
    "MalukuUtara",
    "NusaTenggaraBarat",
    "NusaTenggaraTimur",
    "Papua",
    "PapuaBarat",
    "Riau",
    "SulawesiBarat",
    "SulawesiSelatan",
    "SulawesiTengah",
    "SulawesiTenggara",
    "SulawesiUtara",
    "SumateraBarat",
    "SumateraSelatan",
    "SumateraUtara",
    "Indonesia",
)
expected_sexa_values = (
    "2230",
    "4500",
    "6730",
    "9000",
    "11230",
    "13500",
    "15730",
    "18000",
    "20230",
    "22500",
    "24730",
    "27000",
    "29230",
    "31500",
    "33730",
    "000",
)
expected_type_values = (
    "land",
    "sea",
)
expected_weather_values = (
    0,
    1,
    2,
    3,
    4,
    5,
    10,
    45,
    60,
    61,
    63,
    80,
    95,
    97,
)
expected_cardinal_names = (
    "NORTH",
    "NORTH_NORTHEAST",
    "NORTHEAST",
    "EAST_NORTHEAST",
    "EAST",
    "EAST_SOUTHEAST",
    "SOUTHEAST",
    "SOUTH_SOUTHEAST",
    "SOUTH",
    "SOUTH_SOUTHWEST",
    "SOUTHWEST",
    "WEST_SOUTHWEST",
    "WEST",
    "WEST_NORTHWEST",
    "NORTHWEST",
    "NORTH_NORTHWEST",
    "VARIABLE",
)
expected_province_names = (
    "ACEH",
    "BALI",
    "BANGKA_BELITUNG",
    "BANTEN",
    "BENGKULU",
    "DI_YOGYAKARTA",
    "DKI_JAKARTA",
    "GORONTALO",
    "JAMBI",
    "JAWA_BARAT",
    "JAWA_TENGAH",
    "JAWA_TIMUR",
    "KALIMANTAN_BARAT",
    "KALIMANTAN_SELATAN",
    "KALIMANTAN_TENGAH",
    "KALIMANTAN_TIMUR",
    "KALIMANTAN_UTARA",
    "KEPULAUAN_RIAU",
    "LAMPUNG",
    "MALUKU",
    "MALUKU_UTARA",
    "NUSA_TENGGARA_BARAT",
    "NUSA_TENGGARA_TIMUR",
    "PAPUA",
    "PAPUA_BARAT",
    "RIAU",
    "SULAWESI_BARAT",
    "SULAWESI_SELATAN",
    "SULAWESI_TENGAH",
    "SULAWESI_TENGGARA",
    "SULAWESI_UTARA",
    "SUMATERA_BARAT",
    "SUMATERA_SELATAN",
    "SUMATERA_UTARA",
    "INDONESIA",
)
expected_sexa_names = (
    "NORTH_NORTHEAST",
    "NORTHEAST",
    "EAST_NORTHEAST",
    "EAST",
    "EAST_SOUTHEAST",
    "SOUTHEAST",
    "SOUTH_SOUTHEAST",
    "SOUTH",
    "SOUTH_SOUTHWEST",
    "SOUTHWEST",
    "WEST_SOUTHWEST",
    "WEST",
    "WEST_NORTHWEST",
    "NORTHWEST",
    "NORTH_NORTHWEST",
    "VARIABLE",
)
expected_type_names = (
    "LAND",
    "SEA",
)
expected_weather_names = (
    "CLEAR_SKIES",
    "PARTLY_CLOUDY",
    "PARTLY_CLOUDY2",
    "MOSTLY_CLOUDY",
    "OVERCAST",
    "HAZE",
    "SMOKE",
    "FOG",
    "LIGHT_RAIN",
    "RAIN",
    "HEAVY_RAIN",
    "ISOLATED_SHOWER",
    "SEVERE_THUNDERSTORM",
    "SEVERE_THUNDERSTORM2",
)
expected_enum_names_or_values = chain(
    expected_cardinal_values,
    expected_province_values,
    expected_sexa_values,
    expected_type_values,
    expected_weather_values,
    expected_cardinal_names,
    expected_province_names,
    expected_sexa_names,
    expected_type_names,
    expected_weather_names,
)

actual_cardinal_values = (member.value for member in Cardinal)
actual_province_values = (member.value for member in Province)
actual_sexa_values = (member.value for member in Sexa)
actual_type_values = (member.value for member in Type)
actual_weather_values = (member.value for member in Weather)
actual_cardinal_names = (member.name for member in Cardinal)
actual_province_names = (member.name for member in Province)
actual_sexa_names = (member.name for member in Sexa)
actual_type_names = (member.name for member in Type)
actual_weather_names = (member.name for member in Weather)
actual_enum_names_or_values = chain(
    repeat(actual_cardinal_values, len(expected_cardinal_values)),
    repeat(actual_province_values, len(expected_province_values)),
    repeat(actual_sexa_values, len(expected_sexa_values)),
    repeat(actual_type_values, len(expected_type_values)),
    repeat(actual_weather_values, len(expected_weather_values)),
    repeat(actual_cardinal_names, len(expected_cardinal_names)),
    repeat(actual_province_names, len(expected_province_names)),
    repeat(actual_sexa_names, len(expected_sexa_names)),
    repeat(actual_type_names, len(expected_type_names)),
    repeat(actual_weather_names, len(expected_weather_names)),
)


@pytest.mark.parametrize(
    "expected_enum_name_or_value, actual_enum_names_or_values",
    zip(expected_enum_names_or_values, actual_enum_names_or_values),
)
def test_enum_member_is_contained_in_enum_class(
    expected_enum_name_or_value, actual_enum_names_or_values
):
    assert expected_enum_name_or_value in actual_enum_names_or_values


@pytest.mark.parametrize(
    "enum_class, count",
    ((Cardinal, 17), (Province, 34 + 1), (Sexa, 17 - 1), (Type, 2), (Weather, 12 + 2)),
)
def test_enum_member_count(enum_class, count):
    assert len(enum_class) == count


def test_sexa_not_contain_north():
    assert "NORTH" not in expected_sexa_names
