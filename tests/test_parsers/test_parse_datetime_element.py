from unittest.mock import MagicMock

import pytest

from bmkg.exceptions import WeatherForecastParseError
from bmkg.parsers import parse_datetime_element


def test_parse_element_with_invalid_attribute():
    timerange = MagicMock()
    timerange.get.return_value = None

    element = MagicMock()
    element.__iter__.return_value = [timerange]
    with pytest.raises(
        WeatherForecastParseError, match="datetime attribute in timerange tag not found"
    ):
        for dt in parse_datetime_element(element):
            pass
