from datetime import datetime

# FIXME
# Element is used only for typing not parsing
from xml.etree.ElementTree import Element  # nosec B405

from ..exceptions import WeatherForecastParseError

__all__ = ["parse_issue_element"]


def parse_issue_element(element: Element) -> datetime:
    """
    Parse issue element tree in xml.

    Args:
        element: an element of issue

    Returns:
        A naive `datetime` object.

    Raises:
        WeatherForecastParseError: If some expected attribute is not found.

    Examples:
    >>> from defusedxml.ElementTree import fromstring
    >>> element = fromstring(
    ...     "<issue>"
    ...     "<timestamp>20240116032347</timestamp>"
    ...     "<year>2024</year>"
    ...     "<month>01</month>"
    ...     "<day>16</day>"
    ...     "<hour>03</hour>"
    ...     "<minute>23</minute>"
    ...     "<second>47</second>"
    ...     "</issue>"
    ... )
    >>> issue = parse_issue_element(element)
    >>> issue
    datetime.datetime(2024, 1, 16, 3, 23, 47)
    """
    year_element = element.find("year")
    if year_element is None:
        raise WeatherForecastParseError("year tag in issue tag not found")

    year = year_element.text
    if year is None:
        raise WeatherForecastParseError("year tag in issue tag has no text")

    month_element = element.find("month")
    if month_element is None:
        raise WeatherForecastParseError("month tag in issue tag not found")

    month = month_element.text
    if month is None:
        raise WeatherForecastParseError("month tag in issue tag has no text")

    day_element = element.find("day")
    if day_element is None:
        raise WeatherForecastParseError("day tag in issue tag not found")

    day = day_element.text
    if day is None:
        raise WeatherForecastParseError("day tag in issue tag has no text")

    hour_element = element.find("hour")
    if hour_element is None:
        raise WeatherForecastParseError("hour tag in issue tag not found")

    hour = hour_element.text
    if hour is None:
        raise WeatherForecastParseError("hour tag in issue tag has no text")

    minute_element = element.find("minute")
    if minute_element is None:
        raise WeatherForecastParseError("minute tag in issue tag not found")

    minute = minute_element.text
    if minute is None:
        raise WeatherForecastParseError("minute tag in issue tag has no text")

    second_element = element.find("second")
    if second_element is None:
        raise WeatherForecastParseError("second tag in issue tag not found")

    second = second_element.text
    if second is None:
        raise WeatherForecastParseError("second tag in issue tag has no text")

    timestamp = year + month + day + hour + minute + second

    return datetime.strptime(timestamp, "%Y%m%d%H%M%S")
