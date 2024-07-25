from bmkg import BMKG
from bmkg.api import Earthquake, Shakemap


async def test_when_request_latest_earthquake_then_pass():
    async with BMKG() as bmkg:
        await bmkg.earthquake.get_latest_earthquake()


async def test_when_direct_request_latest_earthquake_then_pass():
    async with Earthquake() as earthquake:
        await earthquake.get_latest_earthquake()


async def test_when_request_latest_earthquake_shakemap_then_pass():
    async with BMKG() as bmkg:
        latest_earthquake = await bmkg.earthquake.get_latest_earthquake()
        await latest_earthquake.shakemap.get_content()


async def test_when_direct_request_latest_earthquake_shakemap_then_pass():
    async with Shakemap("20240203152510.mmi.jpg") as shakemap:
        await shakemap.get_content()


async def test_when_request_strong_earthquake_then_pass():
    async with BMKG() as bmkg:
        list(await bmkg.earthquake.get_strong_earthquake())


async def test_when_direct_request_strong_earthquake_then_pass():
    async with Earthquake() as earthquake:
        list(await earthquake.get_strong_earthquake())


async def test_when_request_felt_earthquake_then_pass():
    async with BMKG() as bmkg:
        list(await bmkg.earthquake.get_felt_earthquake())


async def test_when_direct_request_felt_earthquake_then_pass():
    async with Earthquake() as earthquake:
        list(await earthquake.get_felt_earthquake())
