from unittest.mock import MagicMock

import pytest

from bmkg.exception import WeatherForecastParseError
from bmkg.parsers import parse_forecast_element


def test_parse_element_with_invalid_attribute():
    element = MagicMock()
    element.get.return_value = None

    with pytest.raises(
        WeatherForecastParseError, match="domain attribute in forecast tag not found"
    ):
        parse_forecast_element(element)
