# PyBMKG

[![CI](https://github.com/kiraware/PyBMKG/workflows/ci/badge.svg)](https://github.com/kiraware/PyBMKG/actions/workflows/ci.yml)
[![CodeQL](https://github.com/kiraware/PyBMKG/workflows/CodeQL/badge.svg)](https://github.com/kiraware/PyBMKG/actions/workflows/codeql.yml)
[![Docs](https://readthedocs.org/projects/pybmkg/badge/?version=latest)](https://pybmkg.readthedocs.io/en/latest/?badge=latest)
[![codecov](https://codecov.io/gh/kiraware/PyBMKG/graph/badge.svg?token=MN6AXAHO0P)](https://codecov.io/gh/kiraware/PyBMKG)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)
[![security: bandit](https://img.shields.io/badge/security-bandit-yellow.svg)](https://github.com/PyCQA/bandit)
[![Checked with mypy](http://www.mypy-lang.org/static/mypy_badge.svg)](http://mypy-lang.org/)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![pypi](https://img.shields.io/pypi/v/PyBMKG.svg)](https://pypi.org/project/PyBMKG/)
[![python](https://img.shields.io/pypi/pyversions/PyBMKG.svg)](https://pypi.org/project/PyBMKG/)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/license/MIT)

PyBMKG is an asynchronous Python API wrapper designed to harness the power of BMKG's open data
on weather forecasts and earthquake information in Indonesia. Powered by the Meteorology,
Climatology, and Geophysics Agency ([BMKG](https://bmkg.go.id/)), this project aims to streamline
access to crucial meteorological and seismic data.

## Key Features

- **Asynchronous Operations:** Utilizes `asyncio` and `aiohttp` for efficient API requests.
- **Data Schema:** Built with Python's `dataclass` for clear and structured data representation.
- **Comprehensive Documentation:** Explore detailed [documentation](https://pybmkg.readthedocs.io/en/latest/) for seamless integration and usage.

## Installation

```bash
pip install PyBMKG
```

## Usage

```python
import asyncio

from bmkg import BMKG
from bmkg.enums import Province

async def main():
    async with BMKG() as bmkg:
        weather_forecast = await bmkg.weather_forecast.get_weather_forecast(Province.ACEH)
        latest_earthquake = await bmkg.earthquake.get_latest_earthquake()

        print(f'Weather Forecast: {weather_forecast}')
        print(f'Latest Earthquakes: {latest_earthquake}')

asyncio.run(main())
```

## Table Of Contents

You can start reading the documentation with the
following links:

1. [Tutorials](tutorials.md)
2. [How-To Guides](how-to-guides.md)
3. [Reference](reference/api.md)

## Contributing

We welcome contributions to enhance PyBMKG! Please review our
[contributing guidelines](how-to-guides.md/#contributing)
before getting started.

## Acknowledgements

We would like to thank the Meteorology, Climatology
and Geophysics Agency (BMKG) for its [open data service](https://data.bmkg.go.id/)
on weather forecasts and latest earthquake information.
