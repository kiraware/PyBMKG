from unittest.mock import MagicMock

import pytest

from bmkg.exceptions import WeatherForecastParseError
from bmkg.parsers import parse_weather_element


def test_parse_element_with_invalid_attribute():
    timerange = MagicMock()
    timerange.find.return_value = None

    element = MagicMock()
    element.__iter__.return_value = [timerange]
    with pytest.raises(
        WeatherForecastParseError, match="value tag in timerange tag not found"
    ):
        for _weather in parse_weather_element(element):
            pass


def test_parse_element_with_invalid_weather_text():
    weather = MagicMock()
    weather.text = None

    timerange = MagicMock()
    timerange.find.return_value = weather

    element = MagicMock()
    element.__iter__.return_value = [timerange]
    with pytest.raises(
        WeatherForecastParseError, match="value tag in timerange tag has no text"
    ):
        for _weather in parse_weather_element(element):
            pass
