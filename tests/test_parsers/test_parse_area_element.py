from unittest.mock import MagicMock

import pytest

from bmkg.exception import WeatherForecastParseError
from bmkg.parsers import parse_area_element


@pytest.mark.parametrize(
    "attr, err_msg",
    (
        ("id", "id attribute in area tag not found"),
        ("latitude", "latitude attribute in area tag not found"),
        ("longitude", "longitude attribute in area tag not found"),
        ("type", "type attribute in area tag not found"),
        ("region", "region attribute in area tag not found"),
        ("level", "level attribute in area tag not found"),
        ("description", "description attribute in area tag not found"),
        ("domain", "domain attribute in area tag not found"),
        ("tags", "tags attribute in area tag not found"),
    ),
)
def test_parse_element_with_invalid_attribute(attr, err_msg):
    element = MagicMock()
    element.get.side_effect = lambda x: None if x == attr else MagicMock()

    with pytest.raises(WeatherForecastParseError, match=err_msg):
        parse_area_element(element)


def test_parse_element_with_wrong_names_length():
    element = MagicMock()
    element.findall.__len__.return_value = 1

    with pytest.raises(
        WeatherForecastParseError, match="one or more name tag in area tag not found"
    ):
        parse_area_element(element)


@pytest.mark.parametrize(
    "index, err_msg",
    (
        (0, "name tag in area tag has no text"),
        (1, "name tag in area tag has no text"),
    ),
)
def test_parse_element_with_invalid_en_US_name(index, err_msg):
    names = MagicMock()
    names.__len__.return_value = 2
    names[0].text = MagicMock()
    names[1].text = MagicMock()
    names[index].text = None

    element = MagicMock()
    element.findall.return_value = names

    with pytest.raises(WeatherForecastParseError, match=err_msg):
        parse_area_element(element)
