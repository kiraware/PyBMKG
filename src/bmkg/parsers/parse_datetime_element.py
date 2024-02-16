from collections.abc import Iterator
from datetime import datetime

# FIXME
# Element is used only for typing not parsing
from xml.etree.ElementTree import Element  # nosec B405

from ..exceptions import WeatherForecastParseError

__all__ = ["parse_datetime_element"]


def parse_datetime_element(element: Element) -> Iterator[datetime]:
    """
    Parse datetime element tree in xml.

    This parse datetime string found in element tree in the following format
    `"%Y%m%d%H%M%S"`.

    Args:
        element: any parameter element that contain datetime with type hourly

    Yields:
        Some `datetime` object.

    Raises:
        WeatherForecastParseError: If some expected attribute is not found.

    Examples:
    >>> from defusedxml.ElementTree import fromstring
    >>> element = fromstring(
    ...     '<parameter id="ws" description="datetime" type="hourly">'
    ...     '<timerange type="hourly" h="0" datetime="202401170000">'
    ...     '<value unit="Kt">5</value>'
    ...     '<value unit="MPH">5.75389725</value>'
    ...     '<value unit="KPH">9.26</value>'
    ...     '<value unit="MS">2.57222222</value>'
    ...     "</timerange>"
    ...     '<timerange type="hourly" h="6" datetime="202401170600">'
    ...     '<value unit="Kt">2</value>'
    ...     '<value unit="MPH">2.3015589</value>'
    ...     '<value unit="KPH">3.704</value>'
    ...     '<value unit="MS">1.028888888</value>'
    ...     "</timerange>"
    ...     '<timerange type="hourly" h="12" datetime="202401171200">'
    ...     '<value unit="Kt">0</value>'
    ...     '<value unit="MPH">0</value>'
    ...     '<value unit="KPH">0</value>'
    ...     '<value unit="MS">0</value>'
    ...     "</timerange>"
    ...     "</parameter>"
    ... )
    >>> datetime = parse_datetime_element(element)
    >>> datetime
    <generator object parse_datetime_element at ...>
    """
    for timerange in element:
        dt = timerange.get("datetime")
        if dt is None:
            raise WeatherForecastParseError(
                "datetime attribute in timerange tag not found"
            )

        yield datetime.strptime(dt, "%Y%m%d%H%M%S")
