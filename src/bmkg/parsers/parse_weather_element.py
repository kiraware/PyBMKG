from collections.abc import Iterator

# FIXME
# Element is used only for typing not parsing
from xml.etree.ElementTree import Element  # nosec B405

from .. import enums
from ..exceptions import WeatherForecastParseError

__all__ = ["parse_weather_element"]


def parse_weather_element(element: Element) -> Iterator[enums.Weather]:
    """
    Parse weather element tree in xml.

    Args:
        element: a parameter element that contain weather

    Yields:
        Some `Weather` enum.

    Raises:
        WeatherForecastParseError: If some expected attribute is not found.

    Examples:
    >>> from defusedxml.ElementTree import fromstring
    >>> element = fromstring(
    ...     '<parameter id="weather" description="Weather" type="hourly">'
    ...     '<timerange type="hourly" h="0" datetime="202401170000">'
    ...     '<value unit="icon">60</value>'
    ...     "</timerange>"
    ...     '<timerange type="hourly" h="6" datetime="202401170600">'
    ...     '<value unit="icon">60</value>'
    ...     "</timerange>"
    ...     '<timerange type="hourly" h="12" datetime="202401171200">'
    ...     '<value unit="icon">1</value>'
    ...     "</timerange>"
    ...     "</parameter>"
    ... )
    >>> weather = parse_weather_element(element)
    >>> weather
    <generator object parse_weather_element at ...>
    """
    for timerange in element:
        value_elements = timerange.find("value")
        if value_elements is None:
            raise WeatherForecastParseError("value tag in timerange tag not found")

        weather = value_elements.text
        if weather is None:
            raise WeatherForecastParseError("value tag in timerange tag has no text")

        yield enums.Weather(int(weather))
