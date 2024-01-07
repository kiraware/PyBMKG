from unittest import TestCase

from bmkg.enum.weather_forecast import Cardinal, Province, Sexa, Weather


class TestEnum(TestCase):
    def test_cardinal_enum_value(self):
        values = [member.value for member in Cardinal]

        self.assertIn("N", values)
        self.assertIn("NNE", values)
        self.assertIn("NE", values)
        self.assertIn("ENE", values)
        self.assertIn("E", values)
        self.assertIn("ESE", values)
        self.assertIn("SE", values)
        self.assertIn("SSE", values)
        self.assertIn("S", values)
        self.assertIn("SSW", values)
        self.assertIn("SW", values)
        self.assertIn("WSW", values)
        self.assertIn("W", values)
        self.assertIn("WNW", values)
        self.assertIn("NW", values)
        self.assertIn("NNW", values)
        self.assertIn("VARIABLE", values)

    def test_cardinal_enum_name(self):
        names = [member.name for member in Cardinal]

        self.assertIn("NORTH", names)
        self.assertIn("NORTH_NORTHEAST", names)
        self.assertIn("NORTHEAST", names)
        self.assertIn("EAST_NORTHEAST", names)
        self.assertIn("EAST", names)
        self.assertIn("EAST_SOUTHEAST", names)
        self.assertIn("SOUTHEAST", names)
        self.assertIn("SOUTH_SOUTHEAST", names)
        self.assertIn("SOUTH", names)
        self.assertIn("SOUTH_SOUTHWEST", names)
        self.assertIn("SOUTHWEST", names)
        self.assertIn("WEST_SOUTHWEST", names)
        self.assertIn("WEST", names)
        self.assertIn("WEST_NORTHWEST", names)
        self.assertIn("NORTHWEST", names)
        self.assertIn("NORTH_NORTHWEST", names)
        self.assertIn("VARIABLE", names)

    def test_cardinal_enum_length(self):
        self.assertEqual(len(Cardinal), 17)

    def test_province_enum_value(self):
        values = [member.value for member in Province]

        self.assertIn("Aceh", values)
        self.assertIn("Bali", values)
        self.assertIn("BangkaBelitung", values)
        self.assertIn("Banten", values)
        self.assertIn("Bengkulu", values)
        self.assertIn("DIYogyakarta", values)
        self.assertIn("DKIJakarta", values)
        self.assertIn("Gorontalo", values)
        self.assertIn("Jambi", values)
        self.assertIn("JawaBarat", values)
        self.assertIn("JawaTengah", values)
        self.assertIn("JawaTimur", values)
        self.assertIn("KalimantanBarat", values)
        self.assertIn("KalimantanSelatan", values)
        self.assertIn("KalimantanTengah", values)
        self.assertIn("KalimantanTimur", values)
        self.assertIn("KalimantanUtara", values)
        self.assertIn("KepulauanRiau", values)
        self.assertIn("Lampung", values)
        self.assertIn("Maluku", values)
        self.assertIn("MalukuUtara", values)
        self.assertIn("NusaTenggaraBarat", values)
        self.assertIn("NusaTenggaraTimur", values)
        self.assertIn("Papua", values)
        self.assertIn("PapuaBarat", values)
        self.assertIn("Riau", values)
        self.assertIn("SulawesiBarat", values)
        self.assertIn("SulawesiSelatan", values)
        self.assertIn("SulawesiTengah", values)
        self.assertIn("SulawesiTenggara", values)
        self.assertIn("SulawesiUtara", values)
        self.assertIn("SumateraBarat", values)
        self.assertIn("SumateraSelatan", values)
        self.assertIn("SumateraUtara", values)
        self.assertIn("Indonesia", values)

    def test_province_enum_name(self):
        names = [member.name for member in Province]

        self.assertIn("ACEH", names)
        self.assertIn("BALI", names)
        self.assertIn("BANGKA_BELITUNG", names)
        self.assertIn("BANTEN", names)
        self.assertIn("BENGKULU", names)
        self.assertIn("DI_YOGYAKARTA", names)
        self.assertIn("DKI_JAKARTA", names)
        self.assertIn("GORONTALO", names)
        self.assertIn("JAMBI", names)
        self.assertIn("JAWA_BARAT", names)
        self.assertIn("JAWA_TENGAH", names)
        self.assertIn("JAWA_TIMUR", names)
        self.assertIn("KALIMANTAN_BARAT", names)
        self.assertIn("KALIMANTAN_SELATAN", names)
        self.assertIn("KALIMANTAN_TENGAH", names)
        self.assertIn("KALIMANTAN_TIMUR", names)
        self.assertIn("KALIMANTAN_UTARA", names)
        self.assertIn("KEPULAUAN_RIAU", names)
        self.assertIn("LAMPUNG", names)
        self.assertIn("MALUKU", names)
        self.assertIn("MALUKU_UTARA", names)
        self.assertIn("NUSA_TENGGARA_BARAT", names)
        self.assertIn("NUSA_TENGGARA_TIMUR", names)
        self.assertIn("PAPUA", names)
        self.assertIn("PAPUA_BARAT", names)
        self.assertIn("RIAU", names)
        self.assertIn("SULAWESI_BARAT", names)
        self.assertIn("SULAWESI_SELATAN", names)
        self.assertIn("SULAWESI_TENGAH", names)
        self.assertIn("SULAWESI_TENGGARA", names)
        self.assertIn("SULAWESI_UTARA", names)
        self.assertIn("SUMATERA_BARAT", names)
        self.assertIn("SUMATERA_SELATAN", names)
        self.assertIn("SUMATERA_UTARA", names)
        self.assertIn("INDONESIA", names)

    def test_province_enum_length(self):
        self.assertEqual(len(Province), 34 + 1)

    def test_sexa_enum_value(self):
        values = [member.value for member in Sexa]

        self.assertIn("2230", values)
        self.assertIn("4500", values)
        self.assertIn("6730", values)
        self.assertIn("9000", values)
        self.assertIn("11230", values)
        self.assertIn("13500", values)
        self.assertIn("15730", values)
        self.assertIn("18000", values)
        self.assertIn("20230", values)
        self.assertIn("22500", values)
        self.assertIn("24730", values)
        self.assertIn("27000", values)
        self.assertIn("29230", values)
        self.assertIn("31500", values)
        self.assertIn("33730", values)
        self.assertIn("000", values)

    def test_sexa_enum_name(self):
        names = [member.name for member in Sexa]

        self.assertNotIn("NORTH", names)
        self.assertIn("NORTH_NORTHEAST", names)
        self.assertIn("NORTHEAST", names)
        self.assertIn("EAST_NORTHEAST", names)
        self.assertIn("EAST", names)
        self.assertIn("EAST_SOUTHEAST", names)
        self.assertIn("SOUTHEAST", names)
        self.assertIn("SOUTH_SOUTHEAST", names)
        self.assertIn("SOUTH", names)
        self.assertIn("SOUTH_SOUTHWEST", names)
        self.assertIn("SOUTHWEST", names)
        self.assertIn("WEST_SOUTHWEST", names)
        self.assertIn("WEST", names)
        self.assertIn("WEST_NORTHWEST", names)
        self.assertIn("NORTHWEST", names)
        self.assertIn("NORTH_NORTHWEST", names)
        self.assertIn("VARIABLE", names)

    def test_sexa_enum_length(self):
        self.assertEqual(len(Sexa), 17 - 1)

    def test_weather_enum_value(self):
        values = [member.value for member in Weather]

        self.assertIn(0, values)
        self.assertIn(1, values)
        self.assertIn(2, values)
        self.assertIn(3, values)
        self.assertIn(4, values)
        self.assertIn(5, values)
        self.assertIn(10, values)
        self.assertIn(45, values)
        self.assertIn(60, values)
        self.assertIn(61, values)
        self.assertIn(63, values)
        self.assertIn(80, values)
        self.assertIn(95, values)
        self.assertIn(97, values)

    def test_weather_enum_name(self):
        names = [member.name for member in Weather]

        self.assertIn("CLEAR_SKIES", names)
        self.assertIn("PARTLY_CLOUDY", names)
        self.assertIn("PARTLY_CLOUDY2", names)
        self.assertIn("MOSTLY_CLOUDY", names)
        self.assertIn("OVERCAST", names)
        self.assertIn("HAZE", names)
        self.assertIn("SMOKE", names)
        self.assertIn("FOG", names)
        self.assertIn("LIGHT_RAIN", names)
        self.assertIn("RAIN", names)
        self.assertIn("HEAVY_RAIN", names)
        self.assertIn("ISOLATED_SHOWER", names)
        self.assertIn("SEVERE_THUNDERSTORM", names)
        self.assertIn("SEVERE_THUNDERSTORM2", names)

    def test_weather_enum_length(self):
        self.assertEqual(len(Weather), 12 + 2)
