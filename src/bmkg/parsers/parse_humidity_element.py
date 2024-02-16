from collections.abc import Iterator

# FIXME
# Element is used only for typing not parsing
from xml.etree.ElementTree import Element  # nosec B405

from ..exceptions import WeatherForecastParseError
from ..schemas import Humidity

__all__ = ["parse_humidity_element"]


def parse_humidity_element(element: Element) -> Iterator[Humidity]:
    """
    Parse humidity element tree in xml.

    Args:
        element: a parameter element that contain humidity

    Yields:
        Some `Humidity` schema.

    Raises:
        WeatherForecastParseError: If some expected attribute is not found.

    Examples:
    >>> from defusedxml.ElementTree import fromstring
    >>> element = fromstring(
    ...     '<parameter id="hu" description="Humidity" type="hourly">'
    ...     '<timerange type="hourly" h="0" datetime="202401170000">'
    ...     '<value unit="%">95</value>'
    ...     "</timerange>"
    ...     '<timerange type="hourly" h="6" datetime="202401170600">'
    ...     '<value unit="%">90</value>'
    ...     "</timerange>"
    ...     '<timerange type="hourly" h="12" datetime="202401171200">'
    ...     '<value unit="%">95</value>'
    ...     "</timerange>"
    ...     "</parameter>"
    ... )
    >>> humidity = parse_humidity_element(element)
    >>> humidity
    <generator object parse_humidity_element at ...>
    """
    for timerange in element:
        value_element = timerange.find("value")
        if value_element is None:
            raise WeatherForecastParseError(
                "value tag in timerange tag not found"
            ) from AttributeError

        humidity_text = value_element.text
        if humidity_text is None:
            raise WeatherForecastParseError("value tag in timerange tag has no text")

        yield Humidity(int(humidity_text))
