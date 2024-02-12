from unittest.mock import MagicMock

import pytest

from bmkg.exceptions import WeatherForecastParseError
from bmkg.parsers import parse_temperature_element


def test_parse_element_with_invalid_attribute():
    value_elements = MagicMock()
    value_elements.__len__.return_value = 1

    timerange = MagicMock()
    timerange.findall.return_value = value_elements

    element = MagicMock()
    element.__iter__.return_value = [timerange]
    with pytest.raises(
        WeatherForecastParseError,
        match="one or more value tag in timerange tag not found",
    ):
        for temperature in parse_temperature_element(element):
            pass


@pytest.mark.parametrize(
    "index, err_msg",
    (
        (0, "value tag in timerange tag has no text"),
        (1, "value tag in timerange tag has no text"),
    ),
)
def test_parse_element_with_invalid_value_elements_text(index, err_msg):
    value_element = MagicMock()
    value_element.text = None

    value_elements = MagicMock()
    value_elements.__len__.return_value = 2
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
        for temperature in parse_temperature_element(element):
            pass
