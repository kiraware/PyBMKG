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
    domain = element.get("domain")
    if domain is None:
        raise WeatherForecastParseError("domain attribute in forecast tag not found")

    return Forecast(domain)


def parse_issue_element(element: Element) -> datetime:
    timestamp_element = element.find("timestamp")
    if timestamp_element is None:
        raise WeatherForecastParseError("timestamp tag in issue tag not found")

    timestamp = timestamp_element.text
    if timestamp is None:
        raise WeatherForecastParseError("timestamp tag in issue tag has no text")

    return datetime.strptime(timestamp, "%Y%m%d%H%M%S")


def parse_area_element(element: Element) -> Area:
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
    for timerange in element:
        dt = timerange.get("datetime")
        if dt is None:
            raise WeatherForecastParseError(
                "datetime attribute in timerange tag not found"
            )

        yield datetime.strptime(dt, "%Y%m%d%H%M%S")


def parse_weather_forecast_data(weather_forecast_data: bytes) -> WeatherForecast:
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
        weathers: Iterator[Weather] = iter(())

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
