from collections.abc import Iterator

# FIXME
# Element is used only for typing not parsing
from xml.etree.ElementTree import Element  # nosec B405

from ..exceptions import WeatherForecastParseError
from ..schemas import Temperature

__all__ = ["parse_temperature_element"]


def parse_temperature_element(element: Element) -> Iterator[Temperature]:
    """
    Parse temperature element tree in xml.

    Args:
        element: a parameter element that contain temperature

    Yields:
        Some `Temperature` schema.

    Raises:
        WeatherForecastParseError: If some expected attribute is not found.

    Examples:
    >>> from defusedxml.ElementTree import fromstring
    >>> element = fromstring(
    ...     '<parameter id="t" description="Temperature" type="hourly">'
    ...     '<timerange type="hourly" h="0" datetime="202401170000">'
    ...     '<value unit="C">24</value>'
    ...     '<value unit="F">75.2</value>'
    ...     "</timerange>"
    ...     '<timerange type="hourly" h="6" datetime="202401170600">'
    ...     '<value unit="C">28</value>'
    ...     '<value unit="F">82.4</value>'
    ...     "</timerange>"
    ...     '<timerange type="hourly" h="12" datetime="202401171200">'
    ...     '<value unit="C">26</value>'
    ...     '<value unit="F">78.8</value>'
    ...     "</timerange>"
    ...     "</parameter>"
    ... )
    >>> temperature = parse_temperature_element(element)
    >>> temperature
    <generator object parse_temperature_element at ...>
    """
    for timerange in element:
        value_elements = timerange.findall("value")
        if len(value_elements) < 2:
            raise WeatherForecastParseError(
                "one or more value tag in timerange tag not found"
            )

        celcius = value_elements[0].text
        if celcius is None:
            raise WeatherForecastParseError("value tag in timerange tag has no text")

        fahrenheit = value_elements[1].text
        if fahrenheit is None:
            raise WeatherForecastParseError("value tag in timerange tag has no text")

        yield Temperature(float(celcius), float(fahrenheit))
