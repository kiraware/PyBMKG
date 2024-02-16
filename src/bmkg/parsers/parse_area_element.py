# FIXME
# Element is used only for typing not parsing
from xml.etree.ElementTree import Element  # nosec B405

from ..enums import Type
from ..exceptions import WeatherForecastParseError
from ..schemas import (
    Area,
    Coordinate,
    Name,
)

__all__ = ["parse_area_element"]


def parse_area_element(element: Element) -> Area:
    """
    Parse area element tree in xml.

    Args:
        element: an element of area

    Returns:
        An `Area` schema.

    Raises:
        WeatherForecastParseError: If some expected attribute is not found.

    Examples:
    >>> from defusedxml.ElementTree import fromstring
    >>> element = fromstring(
    ...     "<area"
    ...     ' id="501409"'
    ...     ' latitude="4.176594"'
    ...     ' longitude="96.124878"'
    ...     ' coordinate="96.124878 4.176594"'
    ...     ' type="land"'
    ...     ' region=""'
    ...     ' level="1"'
    ...     ' description="Aceh Barat"'
    ...     ' domain="Aceh"'
    ...     ' tags=""'
    ...     ">"
    ...     '<name xml:lang="en_US">Aceh Barat</name>'
    ...     '<name xml:lang="id_ID">Kab. Aceh Barat</name>'
    ...     "</area>"
    ... )
    >>> area = parse_area_element(element)
    >>> area
    Area(id='501409', coordinate=Coordinate(latitude=4.176594, longitude=96.124878), ...
    """
    id = element.get("id")
    if id is None:
        raise WeatherForecastParseError("id attribute in area tag not found")

    latitude = element.get("latitude")
    if latitude is None:
        raise WeatherForecastParseError("latitude attribute in area tag not found")

    longitude = element.get("longitude")
    if longitude is None:
        raise WeatherForecastParseError("longitude attribute in area tag not found")

    type = element.get("type")
    if type is None:
        raise WeatherForecastParseError("type attribute in area tag not found")

    region = element.get("region")
    if region is None:
        raise WeatherForecastParseError("region attribute in area tag not found")

    level = element.get("level")
    if level is None:
        raise WeatherForecastParseError("level attribute in area tag not found")

    description = element.get("description")
    if description is None:
        raise WeatherForecastParseError("description attribute in area tag not found")

    domain = element.get("domain")
    if domain is None:
        raise WeatherForecastParseError("domain attribute in area tag not found")

    tags = element.get("tags")
    if tags is None:
        raise WeatherForecastParseError("tags attribute in area tag not found")

    names = element.findall("name")
    if len(names) < 2:
        raise WeatherForecastParseError("one or more name tag in area tag not found")

    en_US = names[0].text
    if en_US is None:
        raise WeatherForecastParseError("name tag in area tag has no text")

    id_ID = names[1].text
    if id_ID is None:
        raise WeatherForecastParseError("name tag in area tag has no text")

    name = Name(en_US, id_ID)

    return Area(
        id,
        Coordinate(float(latitude), float(longitude)),
        Type(type),
        region,
        level,
        description,
        domain,
        tags,
        name,
    )
