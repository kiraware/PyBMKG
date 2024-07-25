from unittest.mock import MagicMock

import pytest

from bmkg.exceptions import WeatherForecastParseError
from bmkg.parsers import parse_issue_element


@pytest.mark.parametrize(
    "tag, err_msg",
    (
        ("year", "year tag in issue tag not found"),
        ("month", "month tag in issue tag not found"),
        ("day", "day tag in issue tag not found"),
        ("hour", "hour tag in issue tag not found"),
        ("minute", "minute tag in issue tag not found"),
        ("second", "second tag in issue tag not found"),
    ),
)
def test_parse_element_with_invalid_attribute(tag, err_msg):
    element = MagicMock()
    element.find.side_effect = lambda x: None if x == tag else MagicMock()

    with pytest.raises(WeatherForecastParseError, match=err_msg):
        parse_issue_element(element)


@pytest.mark.parametrize(
    "tag, err_msg",
    (
        ("year", "year tag in issue tag has no text"),
        ("month", "month tag in issue tag has no text"),
        ("day", "day tag in issue tag has no text"),
        ("hour", "hour tag in issue tag has no text"),
        ("minute", "minute tag in issue tag has no text"),
        ("second", "second tag in issue tag has no text"),
    ),
)
def test_parse_element_with_invalid_timestamp_text(tag, err_msg):
    timestamp = MagicMock()
    timestamp.text = None

    element = MagicMock()
    element.find.side_effect = lambda x: timestamp if x == tag else MagicMock()

    with pytest.raises(WeatherForecastParseError, match=err_msg):
        parse_issue_element(element)
