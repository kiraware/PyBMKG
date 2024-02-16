from unittest.mock import MagicMock

import pytest

from bmkg.exceptions import WeatherForecastParseError
from bmkg.parsers import parse_data_element


@pytest.mark.parametrize(
    "attr, err_msg",
    (
        ("source", "source attribute in data tag not found"),
        ("productioncenter", "productioncenter attribute in data tag not found"),
    ),
)
def test_parse_element_with_invalid_attribute(attr, err_msg):
    element = MagicMock()
    element.get.side_effect = lambda x: None if x == attr else MagicMock()

    with pytest.raises(WeatherForecastParseError, match=err_msg):
        parse_data_element(element)
