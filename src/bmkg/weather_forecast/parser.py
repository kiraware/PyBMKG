from collections.abc import Iterator
from datetime import datetime
from itertools import chain

# FIXME
# Element is used only for typing not parsing
from xml.etree.ElementTree import Element  # nosec B405

# FIXME
# remove `type: ignore` if there is a stub for defusedxml
from defusedxml.ElementTree import fromstring  # type: ignore

from ..common.schemas import Coordinate
from .enums import Cardinal, Sexa, Type
from .enums import Weather as WeatherEnum
from .exception import WeatherForecastParseError
from .schemas import (
    Area,
    Data,
    Forecast,
    Humidity,
    Name,
    Temperature,
    Weather,
    WeatherForecast,
    WindDirection,
    WindSpeed,
)
from .types import (
    WeatherForecastParameter,
    WeatherForecastParameterId,
    WeatherForecastParameters,
)

__all__ = [
    "parse_data_element",
    "parse_forecast_element",
    "parse_issue_element",
    "parse_area_element",
    "parse_humidity_element",
    "parse_temperature_element",
    "parse_weather_element",
    "parse_wind_direction_element",
    "parse_wind_speed_element",
    "parse_datetime_element",
    "parse_weather_forecast_data",
]


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
    >>> element = fromstring('<forecast domain="local"></forecast>')
    >>> forecast = parse_forecast_element(element)
    >>> forecast
    Forecast(domain='local')
    """
    domain = element.get("domain")
    if domain is None:
        raise WeatherForecastParseError("domain attribute in forecast tag not found")

    return Forecast(domain)


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


def parse_weather_element(element: Element) -> Iterator[WeatherEnum]:
    """
    Parse weather element tree in xml.

    Args:
        element: a parameter element that contain weather

    Yields:
        Some `Weather` enum.

    Raises:
        WeatherForecastParseError: If some expected attribute is not found.

    Examples:
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
            raise WeatherForecastParseError(
                "value tag in timerange tag not has no text"
            )

        yield WeatherEnum(int(weather))


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


def parse_weather_forecast_data(weather_forecast_data: str | bytes) -> WeatherForecast:
    """
    Parse weather forecast data element tree in xml.

    This control when area type is sea then it has no information regarding weather
    forecast. Also this use wind speed element tree to get the datetime information.

    Args:
        weather_forecast_data: string or bytes of xml data.

    Returns:
        A` WeatherForecast` schema.

    Raises:
        WeatherForecastParseError: If some expected attribute is not found.
    """
    root = fromstring(weather_forecast_data)

    data = parse_data_element(root)

    forecast_element = root[0]
    forecast = parse_forecast_element(forecast_element)

    issue_element = forecast_element[0]
    issue = parse_issue_element(issue_element)

    areas = {}
    for area_element in forecast_element.iterfind("area"):
        area = parse_area_element(area_element)
        # if the area type is sea, then the weather is empty
        weathers: Iterator[Weather] | None = None

        # Only land that has weather, sea doesn't
        if area.type == Type.LAND:
            parameters: WeatherForecastParameters = {}
            for parameter_element in area_element.iterfind("parameter"):
                parameter_id: WeatherForecastParameterId | None = parameter_element.get(
                    "id"
                )
                if parameter_id is None:
                    raise WeatherForecastParseError(
                        "id attribute in parameter tag not found"
                    )

                parameter: WeatherForecastParameter
                if (
                    parameter_id == "hu"
                    or parameter_id == "humax"
                    or parameter_id == "humin"
                ):
                    parameter = parse_humidity_element(parameter_element)
                elif (
                    parameter_id == "t"
                    or parameter_id == "tmax"
                    or parameter_id == "tmin"
                ):
                    parameter = parse_temperature_element(parameter_element)
                elif parameter_id == "weather":
                    parameter = parse_weather_element(parameter_element)
                elif parameter_id == "wd":
                    parameter = parse_wind_direction_element(parameter_element)
                else:
                    # parameter_id == "ws":
                    parameter = parse_wind_speed_element(parameter_element)

                    # Choose one of parameter tag that has datetime attribute with
                    # type hourly. Strictly speaking it is timerange tag.
                    parameters["datetime"] = parse_datetime_element(parameter_element)

                parameters[parameter_id] = parameter

            # The length of the data to be zipped is 12. This is because the weather
            # forecast data received is for three days, each receiving 4 data. However,
            # for tmin, tmax, hmin, and hmax data, these four data are only given 1 each
            # for that day, therefore there are only 3 data for 3 days from tmin, tmax,
            # hmin, and hmax. Because the zip() function will stop at the smallest data
            # length, therefore we need to multiply the 3 data by 4 to get 12
            weathers = (
                Weather(dt, weather, t, tmix, tmax, h, hmin, hmax, wd, ws)
                for dt, weather, t, tmix, tmax, h, hmin, hmax, wd, ws in zip(
                    parameters["datetime"],
                    parameters["weather"],
                    parameters["t"],
                    chain.from_iterable(
                        [(val, val, val, val) for val in parameters["tmin"]]
                    ),
                    chain.from_iterable(
                        [(val, val, val, val) for val in parameters["tmax"]]
                    ),
                    parameters["hu"],
                    chain.from_iterable(
                        [(val, val, val, val) for val in parameters["humin"]]
                    ),
                    chain.from_iterable(
                        [(val, val, val, val) for val in parameters["humax"]]
                    ),
                    parameters["wd"],
                    parameters["ws"],
                )
            )

        areas[area] = weathers

    return WeatherForecast(data, forecast, issue, areas)
