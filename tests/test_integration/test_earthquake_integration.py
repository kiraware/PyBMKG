from bmkg import BMKG


async def test_when_request_latest_earthquake_then_pass_without_error():
    async with BMKG() as bmkg:
        await bmkg.earthquake.get_latest_earthquake()


async def test_when_request_latest_earthquake_shakemap_then_pass_without_error():
    async with BMKG() as bmkg:
        latest_earthquake = await bmkg.earthquake.get_latest_earthquake()
        await latest_earthquake.shakemap.get_content()


async def test_when_request_strong_earthquake_then_pass_without_error():
    async with BMKG() as bmkg:
        list(await bmkg.earthquake.get_strong_earthquake())


async def test_when_request_felt_earthquake_then_pass_without_error():
    async with BMKG() as bmkg:
        list(await bmkg.earthquake.get_felt_earthquake())
