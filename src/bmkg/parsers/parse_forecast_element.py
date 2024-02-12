# FIXME
# Element is used only for typing not parsing
from xml.etree.ElementTree import Element  # nosec B405

from ..exceptions import WeatherForecastParseError
from ..schemas import Forecast

__all__ = ["parse_forecast_element"]


def parse_forecast_element(element: Element) -> Forecast:
    """
    Parse forecast element tree in xml.

    Args:
        element: an element of forecast

    Returns:
        A `Forecast` schema.

    Raises:
        WeatherForecastParseError: If some expected attribute is not found.

    Examples:
    >>> from defusedxml.ElementTree import fromstring
    >>> element = fromstring('<forecast domain="local"></forecast>')
    >>> forecast = parse_forecast_element(element)
    >>> forecast
    Forecast(domain='local')
    """
    domain = element.get("domain")
    if domain is None:
        raise WeatherForecastParseError("domain attribute in forecast tag not found")

    return Forecast(domain)
