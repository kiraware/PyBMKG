"""
Module to store an enum class representation the name of the province.
"""
from enum import Enum

__all__ = ["Province"]


class Province(Enum):
    """
    An enum class that define valid province.

    There are thirty four valid province and one country:
    `ACEH` is `"Aceh"`, `BALI` is `"Bali"`,
    `BANGKA_BELITUNG` is `"BangkaBelitung"`, `BANTEN` is `"Banten"`,
    `BENGKULU` is `"Bengkulu"`, `DI_YOGYAKARTA` is `"DIYogyakarta"`,
    `DKI_JAKARTA` is `"DKIJakarta"`, `GORONTALO` is `"Gorontalo"`,
    `JAMBI` is `"Jambi"`, `JAWA_BARAT` is `"JawaBarat"`,
    `JAWA_TENGAH` is `"JawaTengah"`, `JAWA_TIMUR` is `"JawaTimur"`,
    `KALIMANTAN_BARAT` is `"KalimantanBarat"`,
    `KALIMANTAN_SELATAN` is `"KalimantanSelatan"`,
    `KALIMANTAN_TENGAH` is `"KalimantanTengah"`,
    `KALIMANTAN_TIMUR` is `"KalimantanTimur"`,
    `KALIMANTAN_UTARA` is `"KalimantanUtara"`,
    `KEPULAUAN_RIAU` is `"KepulauanRiau"`, `LAMPUNG` is `"Lampung"`,
    `MALUKU` is `"Maluku"`, `MALUKU_UTARA` is `"MalukuUtara"`,
    `NUSA_TENGGARA_BARAT` is `"NusaTenggaraBarat"`,
    `NUSA_TENGGARA_TIMUR` is `"NusaTenggaraTimur"`, `PAPUA` is `"Papua"`,
    `PAPUA_BARAT` is `"PapuaBarat"`, `RIAU` is `"Riau"`,
    `SULAWESI_BARAT` is `"SulawesiBarat"`,
    `SULAWESI_SELATAN` is `"SulawesiSelatan"`,
    `SULAWESI_TENGAH` is `"SulawesiTengah"`,
    `SULAWESI_TENGGARA` is `"SulawesiTenggara"`,
    `SULAWESI_UTARA` is `"SulawesiUtara"`,
    `SUMATERA_BARAT` is `"SumateraBarat"`,
    `SUMATERA_SELATAN` is `"SumateraSelatan"`,
    `SUMATERA_UTARA` is `"SumateraUtara"`, `INDONESIA` is `"Indonesia"`

    Note `INDONESIA` is the country name
    """

    ACEH = "Aceh"
    BALI = "Bali"
    BANGKA_BELITUNG = "BangkaBelitung"
    BANTEN = "Banten"
    BENGKULU = "Bengkulu"
    DI_YOGYAKARTA = "DIYogyakarta"
    DKI_JAKARTA = "DKIJakarta"
    GORONTALO = "Gorontalo"
    JAMBI = "Jambi"
    JAWA_BARAT = "JawaBarat"
    JAWA_TENGAH = "JawaTengah"
    JAWA_TIMUR = "JawaTimur"
    KALIMANTAN_BARAT = "KalimantanBarat"
    KALIMANTAN_SELATAN = "KalimantanSelatan"
    KALIMANTAN_TENGAH = "KalimantanTengah"
    KALIMANTAN_TIMUR = "KalimantanTimur"
    KALIMANTAN_UTARA = "KalimantanUtara"
    KEPULAUAN_RIAU = "KepulauanRiau"
    LAMPUNG = "Lampung"
    MALUKU = "Maluku"
    MALUKU_UTARA = "MalukuUtara"
    NUSA_TENGGARA_BARAT = "NusaTenggaraBarat"
    NUSA_TENGGARA_TIMUR = "NusaTenggaraTimur"
    PAPUA = "Papua"
    PAPUA_BARAT = "PapuaBarat"
    RIAU = "Riau"
    SULAWESI_BARAT = "SulawesiBarat"
    SULAWESI_SELATAN = "SulawesiSelatan"
    SULAWESI_TENGAH = "SulawesiTengah"
    SULAWESI_TENGGARA = "SulawesiTenggara"
    SULAWESI_UTARA = "SulawesiUtara"
    SUMATERA_BARAT = "SumateraBarat"
    SUMATERA_SELATAN = "SumateraSelatan"
    SUMATERA_UTARA = "SumateraUtara"
    INDONESIA = "Indonesia"
