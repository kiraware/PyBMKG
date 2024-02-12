from collections.abc import Iterator

# FIXME
# Element is used only for typing not parsing
from xml.etree.ElementTree import Element  # nosec B405

from ..enums import Cardinal, Sexa
from ..exceptions import WeatherForecastParseError
from ..schemas import WindDirection

__all__ = ["parse_wind_direction_element"]


def parse_wind_direction_element(element: Element) -> Iterator[WindDirection]:
    """
    Parse wind direction element tree in xml.

    Args:
        element: a parameter element that contain wind direction

    Yields:
        Some `WindDirection` schema.

    Raises:
        WeatherForecastParseError: If some expected attribute is not found.

    Examples:
    >>> from defusedxml.ElementTree import fromstring
    >>> element = fromstring(
    ...     '<parameter id="wd" description="Wind direction" type="hourly">'
    ...     '<timerange type="hourly" h="0" datetime="202401170000">'
    ...     '<value unit="deg">90</value>'
    ...     '<value unit="CARD">E</value>'
    ...     '<value unit="SEXA">9000</value>'
    ...     "</timerange>"
    ...     '<timerange type="hourly" h="6" datetime="202401170600">'
    ...     '<value unit="deg">157.5</value>'
    ...     '<value unit="CARD">SSE</value>'
    ...     '<value unit="SEXA">15730</value>'
    ...     "</timerange>"
    ...     '<timerange type="hourly" h="12" datetime="202401171200">'
    ...     '<value unit="deg">0</value>'
    ...     '<value unit="CARD">VARIABLE</value>'
    ...     '<value unit="SEXA">000</value>'
    ...     "</timerange>"
    ...     "</parameter>"
    ... )
    >>> wind_direction = parse_wind_direction_element(element)
    >>> wind_direction
    <generator object parse_wind_direction_element at ...>
    """
    for timerange in element:
        value_elements = timerange.findall("value")
        if len(value_elements) < 3:
            raise WeatherForecastParseError(
                "one or more value tag in timerange tag not found"
            )

        deg = value_elements[0].text
        if deg is None:
            raise WeatherForecastParseError("value tag in timerange tag has no text")

        card = value_elements[1].text
        if card is None:
            raise WeatherForecastParseError("value tag in timerange tag has no text")

        sexa = value_elements[2].text
        if sexa is None:
            raise WeatherForecastParseError("value tag in timerange tag has no text")

        yield WindDirection(float(deg), Cardinal(card), Sexa(sexa))
