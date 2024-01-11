from bmkg.earthquake import Earthquake


async def test_when_request_latest_earthquake_then_pass_without_error():
    async with Earthquake() as earthquake:
        await earthquake.get_latest_earthquake()


async def test_when_request_latest_earthquake_shakemap_then_pass_without_error():
    async with Earthquake() as earthquake:
        latest_earthquake = await earthquake.get_latest_earthquake()
        await earthquake.get_latest_earthquake_shakemap(latest_earthquake.shakemap)


async def test_when_request_strong_earthquake_then_pass_without_error():
    async with Earthquake() as earthquake:
        list(await earthquake.get_strong_earthquake())


async def test_when_request_felt_earthquake_then_pass_without_error():
    async with Earthquake() as earthquake:
        list(await earthquake.get_felt_earthquake())
