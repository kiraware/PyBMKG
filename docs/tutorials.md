# Tutorial

## Getting Started

Let's install PyBMKG first if it is not already installed
using the following command. Make sure Python is installed
on your computer.

```properties
pip install PyBMKG
```

All done!

## Earthquake API

There are three APIs available for earthquakes
namely get_latest_earthquake, get_strong_earthquake,
and get_felt_earthquake.

### get_latest_earthquake

get_latest_earthquake is used to get latest earthquake
information at `https://data.bmkg.go.id/DataMKG/TEWS/autogempa.json`.
Read get_latest_earthquake
[reference](reference/api.md/#bmkg.api.earthquake.Earthquake.get_latest_earthquake)
for more details.

Code example:

```python
import asyncio
from dataclasses import fields

from bmkg import BMKG


async def main():
    async with BMKG() as bmkg:
        latest_earthquake = await bmkg.earthquake.get_latest_earthquake()

        print(latest_earthquake.earthquake.datetime)
        print(latest_earthquake.earthquake.coordinate)
        print(
            latest_earthquake.earthquake.magnitude,
            fields(latest_earthquake.earthquake)[2].metadata["unit"],
        )
        print(
            latest_earthquake.earthquake.depth,
            fields(latest_earthquake.earthquake)[3].metadata["unit"],
        )
        print(latest_earthquake.earthquake.region)
        print(latest_earthquake.potency)
        print(latest_earthquake.felt)
        print(latest_earthquake.shakemap)

asyncio.run(main())
```

Example output:

```console
2024-01-17 18:29:39+00:00
Coordinate(latitude=-3.63, longitude=140.46)
5.0 M
62.0 km
46 km BaratDaya KEEROM-PAPUA
Tidak berpotensi tsunami
-
Shakemap(file_name='20240118013237.mmi.jpg')
```

### get_strong_earthquake

get_strong_earthquake is used to get fifteen strong earthquake
information with a magnitude of 5.0 M and above at
`https://data.bmkg.go.id/DataMKG/TEWS/gempaterkini.json`.
Read get_strong_earthquake
[reference](reference/api.md/#bmkg.api.earthquake.Earthquake.get_strong_earthquake)
for more details.

Code example:

```python
import asyncio
from dataclasses import fields

from bmkg import BMKG


async def main():
    async with BMKG() as bmkg:
        strong_earthquakes = await bmkg.earthquake.get_strong_earthquake()

        for strong_earthquake in strong_earthquakes:
            print(strong_earthquake.earthquake.datetime)
            print(strong_earthquake.earthquake.coordinate)
            print(
                strong_earthquake.earthquake.magnitude,
                fields(strong_earthquake.earthquake)[2].metadata["unit"],
            )
            print(
                strong_earthquake.earthquake.depth,
                fields(strong_earthquake.earthquake)[3].metadata["unit"],
            )
            print(strong_earthquake.earthquake.region)
            print(strong_earthquake.potency)

asyncio.run(main())
```

Example output:

```console
2024-01-17 18:29:39+00:00
Coordinate(latitude=-3.63, longitude=140.46)
5.0 M
62.0 km
46 km BaratDaya KEEROM-PAPUA
Tidak berpotensi tsunami
...
```

### get_felt_earthquake

get_felt_earthquake is used to get fifteen felt earthquake
information at `https://data.bmkg.go.id/DataMKG/TEWS/gempadirasakan.json`.
Read get_felt_earthquake
[reference](reference/api.md/#bmkg.api.earthquake.Earthquake.get_felt_earthquake)
for more details.

Code example:

```python
import asyncio
from dataclasses import fields

from bmkg import BMKG


async def main():
    async with BMKG() as bmkg:
        felt_earthquakes = await bmkg.earthquake.get_felt_earthquake()

        for felt_earthquake in felt_earthquakes:
            print(felt_earthquake.earthquake.datetime)
            print(felt_earthquake.earthquake.coordinate)
            print(
                felt_earthquake.earthquake.magnitude,
                fields(felt_earthquake.earthquake)[2].metadata["unit"],
            )
            print(
                felt_earthquake.earthquake.depth,
                fields(felt_earthquake.earthquake)[3].metadata["unit"],
            )
            print(felt_earthquake.earthquake.region)
            print(felt_earthquake.felt)

asyncio.run(main())
```

Example output:

```console
2024-01-17 15:18:05+00:00
Coordinate(latitude=3.89, longitude=95.84)
4.9 M
27.0 km
Pusat gempa berada di laut 42 Km Barat Daya Meulaboh-Aceh Barat
III Banda Aceh, II-III Calang Aceh Jaya, II-III Aceh Besar
...
```

## Shakemap API

Shakemap API is part of the earthquake API. There is one method
that the shakemap API has, namely the get_content method.

### get_content

get_content is used to get latest earthquake shake map.
The link starts with `https://data.bmkg.go.id/DataMKG/TEWS/`
and followed with shakemap filename. Read get_content
[reference](reference/api.md/#bmkg.api.shakemap.Shakemap.get_content)
for more details.

Code example:

```python
import asyncio

from bmkg import BMKG


async def main():
    async with BMKG() as bmkg:
        latest_earthquake = await bmkg.earthquake.get_latest_earthquake()
        shakemap = latest_earthquake.shakemap
        shakemap_content = await shakemap.get_content()

        print(shakemap.file_name)
        print(shakemap_content)

asyncio.run(main())
```

Example output:

```console
20240203152510.mmi.jpg
b'\xff\xd8\xff\xe0\x00\x10JFIF\x00\x01\x01\x01\x00...'
```

## Weather Forecast API

There is only one API available for weather forecast
namely get_weather_forecast.

### get_weather_forecast

get_weather_forecast is used to get weather forecast
information for all districts and cities in Indonesia
within three days. There are 35 weather forecast data
representing provinces and major cities in Indonesia.
For each area you will get twelve weather forecasts data
so there are four weather forecasts for one day. The link
starts with `https://data.bmkg.go.id/DataMKG/MEWS/DigitalForecast/`
and followed with `DigitalForecast-{PROVINCE_NAME}.xml`. Read
get_weather_forecast [reference](reference/api.md/#bmkg.api.weather_forecast.WeatherForecast.get_weather_forecast)
for more details.

Code example:

```python
import asyncio

from bmkg import BMKG
from bmkg.enums import Province, Type


async def main():
    async with BMKG() as bmkg:
        weather_forecast_data = await bmkg.weather_forecast.get_weather_forecast(Province.ACEH)

        print(weather_forecast_data.data)
        print(weather_forecast_data.forecast)
        print(weather_forecast_data.issue)

        for area, weathers in weather_forecast_data.weathers.items():
            if area.type == Type.LAND:
                print(area)

                for weather in weathers:
                    print(weather.datetime)
                    print(weather.weather)
                    print(weather.temperature)
                    print(weather.minimum_temperature)
                    print(weather.maximum_temperature)
                    print(weather.humidity)
                    print(weather.min_humidity)
                    print(weather.max_humidity)
                    print(weather.wind_direction)
                    print(weather.wind_speed)

asyncio.run(main())
```

Example output:

```console
Data(source='meteofactory', productioncenter='NC Jakarta')
Forecast(domain='local')
2024-01-18 03:13:02
Area(id='501409', coordinate=Coordinate(latitude=4.176594, longitude=96.124878), type=<Type.LAND: 'land'>, region='', level='1', description='Aceh Barat', domain='Aceh', tags='', names=Name(en_US='Aceh Barat', id_ID='Kab. Aceh Barat'))
2024-01-18 00:00:00
1
Temperature(celcius=25.0, fahrenheit=77.0)
Temperature(celcius=25.0, fahrenheit=77.0)
Temperature(celcius=32.0, fahrenheit=89.6)
Humidity(percentage=95)
Humidity(percentage=60)
Humidity(percentage=95)
WindDirection(deg=67.5, card=<Cardinal.EAST_NORTHEAST: 'ENE'>, sexa=<Sexa.EAST_NORTHEAST: '6730'>)
WindSpeed(knot=5.0, mph=5.75389725, kph=9.26, ms=2.57222222)
...
```
