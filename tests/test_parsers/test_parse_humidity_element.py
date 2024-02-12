from unittest.mock import MagicMock

import pytest

from bmkg.exceptions import WeatherForecastParseError
from bmkg.parsers import parse_humidity_element


def test_parse_element_with_invalid_attribute():
    timerange = MagicMock()
    timerange.find.return_value = None

    element = MagicMock()
    element.__iter__.return_value = [timerange]
    with pytest.raises(
        WeatherForecastParseError, match="value tag in timerange tag not found"
    ):
        for humidity in parse_humidity_element(element):
            pass


def test_parse_element_with_invalid_humidity_text():
    humidity = MagicMock()
    humidity.text = None

    timerange = MagicMock()
    timerange.find.return_value = humidity

    element = MagicMock()
    element.__iter__.return_value = [timerange]
    with pytest.raises(
        WeatherForecastParseError, match="value tag in timerange tag has no text"
    ):
        for humidity in parse_humidity_element(element):
            pass
