import pytest

from bmkg.exceptions import WeatherForecastParseError
from bmkg.parsers import parse_weather_forecast_data


def test_parse_element_with_invalid_attribute():
    with pytest.raises(
        WeatherForecastParseError, match="id attribute in parameter tag not found"
    ):
        parse_weather_forecast_data(
            '<data source="meteofactory" productioncenter="NC Jakarta">'
            "  <forecast domain='local'>"
            "    <issue>"
            "      <timestamp>20240216023745</timestamp>"
            "      <year>2024</year>"
            "      <month>02</month>"
            "      <day>16</day>"
            "      <hour>02</hour>"
            "      <minute>37</minute>"
            "      <second>45</second>"
            "    </issue>"
            "    <area"
            '      id="501409"'
            '      latitude="4.176594"'
            '      longitude="96.124878"'
            '      coordinate="96.124878 4.176594"'
            '      type="land"'
            '      region=""'
            '      level="1"'
            '      description="Aceh Barat"'
            '      domain="Aceh"'
            '      tags=""'
            "    >"
            '      <name xml:lang="en_US">Aceh Barat</name>'
            '      <name xml:lang="id_ID">Kab. Aceh Barat</name>'
            '      <parameter description="Humidity" type="hourly">'
            "      </parameter>"
            "    </area>"
            "  </forecast>"
            "</data>"
        )
