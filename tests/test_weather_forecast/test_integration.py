import pytest

from bmkg.enum.weather_forecast import Province
from bmkg.weather_forecast.weather_forecast import WeatherForecast


@pytest.mark.parametrize("province", Province)
async def test_given_provinces_when_request_weather_forecast_then_pass_without_error(
    province,
):
    async with WeatherForecast() as weather_forecast:
        await weather_forecast.get_weather_forecast(province)
