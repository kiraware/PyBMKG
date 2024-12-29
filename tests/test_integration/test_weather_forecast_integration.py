from bmkg import WeatherForecast


async def test_given_provinces_when_direct_request_weather_forecast_then_pass():
    async with WeatherForecast() as weather_forecast:
        await weather_forecast.get_weather_forecast("11.01.01.2001")
