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
    timestamp_element = element.find("timestamp")
    if timestamp_element is None:
        raise WeatherForecastParseError("timestamp tag in issue tag not found")

    timestamp = timestamp_element.text
    if timestamp is None:
        raise WeatherForecastParseError("timestamp tag in issue tag has no text")

    return datetime.strptime(timestamp, "%Y%m%d%H%M%S")
