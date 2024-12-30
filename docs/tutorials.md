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
information at `https://data.bmkg.go.id/DataMKG/TEWS/autogempa.json`. Read
[get_latest_earthquake reference](reference/api.md/#bmkg.api.Earthquake.get_latest_earthquake)
for more details.

!!! example

    ```python
    import asyncio
    from dataclasses import fields

    from bmkg import Earthquake


    async def main():
        async with Earthquake() as earthquake:
            latest_earthquake = await earthquake.get_latest_earthquake()

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

    Output:

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
`https://data.bmkg.go.id/DataMKG/TEWS/gempaterkini.json`. Read
[get_strong_earthquake reference](reference/api.md/#bmkg.api.Earthquake.get_strong_earthquake)
for more details.

!!! example

    ```python
    import asyncio
    from dataclasses import fields

    from bmkg import Earthquake


    async def main():
        async with Earthquake() as earthquake:
            strong_earthquakes = await earthquake.get_strong_earthquake()

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

    Output:

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
information at `https://data.bmkg.go.id/DataMKG/TEWS/gempadirasakan.json`. Read
[get_felt_earthquake reference](reference/api.md/#bmkg.api.Earthquake.get_felt_earthquake)
for more details.

!!! example

    ```python
    import asyncio
    from dataclasses import fields

    from bmkg import Earthquake


    async def main():
        async with Earthquake() as earthquake:
            felt_earthquakes = await earthquake.get_felt_earthquake()

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

    Output:

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
The link starts with `https://data.bmkg.go.id/DataMKG/TEWS`
and followed with `/shakemap-filename`. Read
[get_content reference](reference/api.md/#bmkg.api.Shakemap.get_content)
for more details.

!!! example

    ```python
    import asyncio

    from bmkg import Shakemap


    async def main():
        async with Shakemap("20240203152510.mmi.jpg") as shakemap:
            shakemap_content = await shakemap.get_content()

            print(shakemap.file_name)
            print(shakemap_content)

    asyncio.run(main())
    ```

    Output:

    ```console
    20240203152510.mmi.jpg
    b'\xff\xd8\xff\xe0\x00\x10JFIF\x00\x01\x01\x01\x00...'
    ```

## Weather Forecast API

There is only one API available for weather forecast
namely get_weather_forecast.

### get_weather_forecast

get_weather_forecast provides weather forecast information for all districts
and cities across Indonesia, covering a three-day period. The data is organized
by region, identified using a unique "Region IV" code, which follows the format
W.X.Y.Z (e.g., "11.01.01.2001"). A comprehensive list of available region codes
can be found at [kodewilayah.id](https://kodewilayah.id).

The forecast includes detailed weather information for each region, with
updates every three hours for the next three days. The weather data is
refreshed every two days. To access the forecast, use the API endpoint
`https://api.bmkg.go.id/publik/prakiraan-cuaca?adm4={region_code}`. Read
[get_weather_forecast reference](reference/api.md/#bmkg.api.WeatherForecast.get_weather_forecast)
for more details.

!!! example

    ```python
    import asyncio

    from bmkg import WeatherForecast


    async def main():
        async with WeatherForecast() as weather_forecast:
            weather_forecast = await weather_forecast.get_weather_forecast("11.01.01.2001")

            print(weather_forecast.location)

            for weather in weather_forecast.weathers:
                print(weather)

    asyncio.run(main())
    ```

    Output:

    ```console
    Location(admin_level_1='11', admin_level_2='11.01', admin_level_3='11.01.01', admin_level_4='11.01.01.2001', province='Aceh', city='Aceh Selatan', subdistrict='Bakongan', village='Keude Bakongan', longitude=97.4845840426, latitude=2.9310948032, timezone='Asia/Jakarta')
    Weather(datetime=datetime.datetime(2024, 12, 29, 0, 0, tzinfo=datetime.timezone.utc), t=24, tcc=100, tp=0.0, weather=<Weather.MOSTLY_CLOUDY: 3>, wd_deg=72, wd=<Cardinal.NORTHEAST: 'NE'>, wd_to=<Cardinal.SOUTHWEST: 'SW'>, ws=4.0, hu=95, vs=18158, time_index='-3-0', analysis_date=datetime.datetime(2024, 12, 29, 0, 0), image='https://api-apps.bmkg.go.id/storage/icon/cuaca/berawan-am.svg', utc_datetime=datetime.datetime(2024, 12, 29, 0, 0), local_datetime=datetime.datetime(2024, 12, 29, 7, 0))
    Weather(datetime=datetime.datetime(2024, 12, 29, 3, 0, tzinfo=datetime.timezone.utc), t=28, tcc=100, tp=0.0, weather=<Weather.MOSTLY_CLOUDY: 3>, wd_deg=171, wd=<Cardinal.SOUTHEAST: 'SE'>, wd_to=<Cardinal.NORTHWEST: 'NW'>, ws=2.9, hu=78, vs=45315, time_index='0-3', analysis_date=datetime.datetime(2024, 12, 29, 0, 0), image='https://api-apps.bmkg.go.id/storage/icon/cuaca/berawan-am.svg', utc_datetime=datetime.datetime(2024, 12, 29, 3, 0), local_datetime=datetime.datetime(2024, 12, 29, 10, 0))
    Weather(datetime=datetime.datetime(2024, 12, 29, 6, 0, tzinfo=datetime.timezone.utc), t=28, tcc=99, tp=0.8, weather=<Weather.MOSTLY_CLOUDY: 3>, wd_deg=205, wd=<Cardinal.SOUTH: 'S'>, wd_to=<Cardinal.NORTH: 'N'>, ws=8.5, hu=77, vs=23196, time_index='3-6', analysis_date=datetime.datetime(2024, 12, 29, 0, 0), image='https://api-apps.bmkg.go.id/storage/icon/cuaca/berawan-am.svg', utc_datetime=datetime.datetime(2024, 12, 29, 6, 0), local_datetime=datetime.datetime(2024, 12, 29, 13, 0))
    Weather(datetime=datetime.datetime(2024, 12, 29, 9, 0, tzinfo=datetime.timezone.utc), t=28, tcc=100, tp=1.3, weather=<Weather.MOSTLY_CLOUDY: 3>, wd_deg=89, wd=<Cardinal.NORTHEAST: 'NE'>, wd_to=<Cardinal.SOUTHWEST: 'SW'>, ws=1.9, hu=81, vs=29860, time_index='6-9', analysis_date=datetime.datetime(2024, 12, 29, 0, 0), image='https://api-apps.bmkg.go.id/storage/icon/cuaca/berawan-am.svg', utc_datetime=datetime.datetime(2024, 12, 29, 9, 0), local_datetime=datetime.datetime(2024, 12, 29, 16, 0))
    Weather(datetime=datetime.datetime(2024, 12, 29, 12, 0, tzinfo=datetime.timezone.utc), t=26, tcc=100, tp=1.2, weather=<Weather.MOSTLY_CLOUDY: 3>, wd_deg=141, wd=<Cardinal.SOUTHEAST: 'SE'>, wd_to=<Cardinal.NORTHWEST: 'NW'>, ws=7.7, hu=90, vs=14741, time_index='9-12', analysis_date=datetime.datetime(2024, 12, 29, 0, 0), image='https://api-apps.bmkg.go.id/storage/icon/cuaca/berawan-am.svg', utc_datetime=datetime.datetime(2024, 12, 29, 12, 0), local_datetime=datetime.datetime(2024, 12, 29, 19, 0))
    Weather(datetime=datetime.datetime(2024, 12, 29, 15, 0, tzinfo=datetime.timezone.utc), t=25, tcc=99, tp=2.1, weather=<Weather.MOSTLY_CLOUDY: 3>, wd_deg=112, wd=<Cardinal.EAST: 'E'>, wd_to=<Cardinal.WEST: 'W'>, ws=6.1, hu=90, vs=15254, time_index='12-15', analysis_date=datetime.datetime(2024, 12, 29, 0, 0), image='https://api-apps.bmkg.go.id/storage/icon/cuaca/berawan-am.svg', utc_datetime=datetime.datetime(2024, 12, 29, 15, 0), local_datetime=datetime.datetime(2024, 12, 29, 22, 0))
    ...
    ```
