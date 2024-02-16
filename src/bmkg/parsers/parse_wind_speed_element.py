from collections.abc import Iterator

# FIXME
# Element is used only for typing not parsing
from xml.etree.ElementTree import Element  # nosec B405

from ..exceptions import WeatherForecastParseError
from ..schemas import WindSpeed

__all__ = ["parse_wind_speed_element"]


def parse_wind_speed_element(element: Element) -> Iterator[WindSpeed]:
    """
    Parse wind speed element tree in xml.

    Args:
        element: a parameter element that contain wind speed

    Yields:
        Some `WindSpeed` schema.

    Raises:
        WeatherForecastParseError: If some expected attribute is not found.

    Examples:
    >>> from defusedxml.ElementTree import fromstring
    >>> element = fromstring(
    ...     '<parameter id="ws" description="Wind speed" type="hourly">'
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
    >>> wind_speed = parse_wind_speed_element(element)
    >>> wind_speed
    <generator object parse_wind_speed_element at ...>
    """
    for timerange in element:
        value_elements = timerange.findall("value")
        if len(value_elements) < 4:
            raise WeatherForecastParseError(
                "one or more value tag in timerange tag not found"
            )

        knot = value_elements[0].text
        if knot is None:
            raise WeatherForecastParseError("value tag in timerange tag has no text")

        mph = value_elements[1].text
        if mph is None:
            raise WeatherForecastParseError("value tag in timerange tag has no text")

        kph = value_elements[2].text
        if kph is None:
            raise WeatherForecastParseError("value tag in timerange tag has no text")

        ms = value_elements[3].text
        if ms is None:
            raise WeatherForecastParseError("value tag in timerange tag has no text")

        yield WindSpeed(float(knot), float(mph), float(kph), float(ms))
