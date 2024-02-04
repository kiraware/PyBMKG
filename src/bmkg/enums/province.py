"""
Module to store a str enum class representation the name of the province.
"""
from enum import StrEnum

__all__ = ["Province"]


class Province(StrEnum):
    """
    A str enum class that define valid province.

    Attributes:
        ACEH: `"Aceh"`
        BALI: `"Bali"`
        BANGKA_BELITUNG: `"BangkaBelitung"`
        BANTEN: `"Banten"`
        BENGKULU: `"Bengkulu"`
        DI_YOGYAKARTA: `"DIYogyakarta"`
        DKI_JAKARTA: `"DKIJakarta"`
        GORONTALO: `"Gorontalo"`
        JAMBI: `"Jambi"`
        JAWA_BARAT: `"JawaBarat"`
        JAWA_TENGAH: `"JawaTengah"`
        JAWA_TIMUR: `"JawaTimur"`
        KALIMANTAN_BARAT: `"KalimantanBarat"`
        KALIMANTAN_SELATAN: `"KalimantanSelatan"`
        KALIMANTAN_TENGAH: `"KalimantanTengah"`
        KALIMANTAN_TIMUR: `"KalimantanTimur"`
        KALIMANTAN_UTARA: `"KalimantanUtara"`
        KEPULAUAN_RIAU: `"KepulauanRiau"`
        LAMPUNG: `"Lampung"`
        MALUKU: `"Maluku"`
        MALUKU_UTARA: `"MalukuUtara"`
        NUSA_TENGGARA_BARAT: `"NusaTenggaraBarat"`
        NUSA_TENGGARA_TIMUR: `"NusaTenggaraTimur"`
        PAPUA: `"Papua"`
        PAPUA_BARAT: `"PapuaBarat"`
        RIAU: `"Riau"`
        SULAWESI_BARAT: `"SulawesiBarat"`
        SULAWESI_SELATAN: `"SulawesiSelatan"`
        SULAWESI_TENGAH: `"SulawesiTengah"`
        SULAWESI_TENGGARA: `"SulawesiTenggara"`
        SULAWESI_UTARA: `"SulawesiUtara"`
        SUMATERA_BARAT: `"SumateraBarat"`
        SUMATERA_SELATAN: `"SumateraSelatan"`
        SUMATERA_UTARA: `"SumateraUtara"`
        INDONESIA: `"Indonesia"`

    Examples:
        >>> Province("Aceh")
        <Province.ACEH: 'Aceh'>
        >>> Province["ACEH"]
        <Province.ACEH: 'Aceh'>
        >>> Province.ACEH
        <Province.ACEH: 'Aceh'>
        >>> Province.ACEH == "Aceh"
        True
        >>> print(Province.ACEH)
        Aceh

    Note:
        `INDONESIA` is the country name.
    """

    ACEH: str = "Aceh"
    BALI: str = "Bali"
    BANGKA_BELITUNG: str = "BangkaBelitung"
    BANTEN: str = "Banten"
    BENGKULU: str = "Bengkulu"
    DI_YOGYAKARTA: str = "DIYogyakarta"
    DKI_JAKARTA: str = "DKIJakarta"
    GORONTALO: str = "Gorontalo"
    JAMBI: str = "Jambi"
    JAWA_BARAT: str = "JawaBarat"
    JAWA_TENGAH: str = "JawaTengah"
    JAWA_TIMUR: str = "JawaTimur"
    KALIMANTAN_BARAT: str = "KalimantanBarat"
    KALIMANTAN_SELATAN: str = "KalimantanSelatan"
    KALIMANTAN_TENGAH: str = "KalimantanTengah"
    KALIMANTAN_TIMUR: str = "KalimantanTimur"
    KALIMANTAN_UTARA: str = "KalimantanUtara"
    KEPULAUAN_RIAU: str = "KepulauanRiau"
    LAMPUNG: str = "Lampung"
    MALUKU: str = "Maluku"
    MALUKU_UTARA: str = "MalukuUtara"
    NUSA_TENGGARA_BARAT: str = "NusaTenggaraBarat"
    NUSA_TENGGARA_TIMUR: str = "NusaTenggaraTimur"
    PAPUA: str = "Papua"
    PAPUA_BARAT: str = "PapuaBarat"
    RIAU: str = "Riau"
    SULAWESI_BARAT: str = "SulawesiBarat"
    SULAWESI_SELATAN: str = "SulawesiSelatan"
    SULAWESI_TENGAH: str = "SulawesiTengah"
    SULAWESI_TENGGARA: str = "SulawesiTenggara"
    SULAWESI_UTARA: str = "SulawesiUtara"
    SUMATERA_BARAT: str = "SumateraBarat"
    SUMATERA_SELATAN: str = "SumateraSelatan"
    SUMATERA_UTARA: str = "SumateraUtara"
    INDONESIA: str = "Indonesia"
