from unittest.mock import MagicMock

import pytest

from bmkg.exceptions import WeatherForecastParseError
from bmkg.parsers import parse_wind_speed_element


def test_parse_element_with_invalid_attribute():
    value_elements = MagicMock()
    value_elements.__len__.return_value = 3

    timerange = MagicMock()
    timerange.findall.return_value = value_elements

    element = MagicMock()
    element.__iter__.return_value = [timerange]
    with pytest.raises(
        WeatherForecastParseError,
        match="one or more value tag in timerange tag not found",
    ):
        for wind_speed in parse_wind_speed_element(element):
            pass


@pytest.mark.parametrize(
    "index, err_msg",
    (
        (0, "value tag in timerange tag has no text"),
        (1, "value tag in timerange tag has no text"),
        (2, "value tag in timerange tag has no text"),
        (3, "value tag in timerange tag has no text"),
    ),
)
def test_parse_element_with_invalid_value_elements_text(index, err_msg):
    value_element = MagicMock()
    value_element.text = None

    value_elements = MagicMock()
    value_elements.__len__.return_value = 4
    value_elements.__getitem__.side_effect = (
        lambda idx: value_element if idx == index else MagicMock()
    )

    timerange = MagicMock()
    timerange.findall.return_value = value_elements

    element = MagicMock()
    element.__iter__.return_value = [timerange]
    with pytest.raises(
        WeatherForecastParseError,
        match=err_msg,
    ):
        for wind_speed in parse_wind_speed_element(element):
            pass
