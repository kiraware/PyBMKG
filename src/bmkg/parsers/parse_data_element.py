# FIXME
# Element is used only for typing not parsing
from xml.etree.ElementTree import Element  # nosec B405

from ..exceptions import WeatherForecastParseError
from ..schemas import Data

__all__ = ["parse_data_element"]


def parse_data_element(element: Element) -> Data:
    """
    Parse data element tree in xml.

    Args:
        element: an element of data

    Returns:
        A `Data` schema.

    Raises:
        WeatherForecastParseError: If some expected attribute is not found.

    Examples:
    >>> from defusedxml.ElementTree import fromstring
    >>> element = fromstring(
    ...     '<data source="meteofactory" productioncenter="NC Jakarta"></data>'
    ... )
    >>> data = parse_data_element(element)
    >>> data
    Data(source='meteofactory', productioncenter='NC Jakarta')
    """
    source = element.get("source")
    if source is None:
        raise WeatherForecastParseError("source attribute in data tag not found")

    productioncenter = element.get("productioncenter")
    if productioncenter is None:
        raise WeatherForecastParseError(
            "productioncenter attribute in data tag not found"
        )

    return Data(source, productioncenter)
