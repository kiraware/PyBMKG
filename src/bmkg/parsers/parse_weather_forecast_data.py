from collections.abc import Iterator
from itertools import chain

# FIXME
# remove `type: ignore` if there is a stub for defusedxml
from defusedxml.ElementTree import fromstring  # type: ignore

from ..enums import Type
from ..exceptions import WeatherForecastParseError
from ..schemas import (
    Weather,
    WeatherForecast,
)
from ..types import (
    WeatherForecastParameter,
    WeatherForecastParameterId,
    WeatherForecastParameters,
)
from .parse_area_element import parse_area_element
from .parse_data_element import parse_data_element
from .parse_datetime_element import parse_datetime_element
from .parse_forecast_element import parse_forecast_element
from .parse_humidity_element import parse_humidity_element
from .parse_issue_element import parse_issue_element
from .parse_temperature_element import parse_temperature_element
from .parse_weather_element import parse_weather_element
from .parse_wind_direction_element import parse_wind_direction_element
from .parse_wind_speed_element import parse_wind_speed_element

__all__ = ["parse_weather_forecast_data"]


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
