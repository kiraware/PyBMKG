import pytest

from bmkg import BMKG
from bmkg.api import WeatherForecast
from bmkg.enums import Province, Type


@pytest.mark.parametrize("province", Province)
async def test_given_provinces_when_request_weather_forecast_then_pass(province):
    async with BMKG() as bmkg:
        weather_forecast_data = await bmkg.weather_forecast.get_weather_forecast(
            province
        )
        for area, weather in weather_forecast_data.weathers.items():
            if area.type == Type.LAND:
                list(weather)


@pytest.mark.parametrize("province", Province)
async def test_given_provinces_when_direct_request_weather_forecast_then_pass(province):
    async with WeatherForecast() as weather_forecast:
        weather_forecast_data = await weather_forecast.get_weather_forecast(province)
        for area, weather in weather_forecast_data.weathers.items():
            if area.type == Type.LAND:
                list(weather)
