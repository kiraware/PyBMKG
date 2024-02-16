# PyBMKG

[![CI](https://github.com/kiraware/PyBMKG/workflows/ci/badge.svg)](https://github.com/kiraware/PyBMKG/actions/workflows/ci.yml)
[![CodeQL](https://github.com/kiraware/PyBMKG/workflows/codeql/badge.svg)](https://github.com/kiraware/PyBMKG/actions/workflows/codeql.yml)
[![Docs](https://readthedocs.org/projects/pybmkg/badge/?version=latest)](https://pybmkg.readthedocs.io/en/latest/?badge=latest)
[![codecov](https://codecov.io/gh/kiraware/PyBMKG/graph/badge.svg?token=MN6AXAHO0P)](https://codecov.io/gh/kiraware/PyBMKG)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)
[![security: bandit](https://img.shields.io/badge/security-bandit-yellow.svg)](https://github.com/PyCQA/bandit)
[![Checked with mypy](http://www.mypy-lang.org/static/mypy_badge.svg)](http://mypy-lang.org/)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![pypi](https://img.shields.io/pypi/v/PyBMKG.svg)](https://pypi.org/project/PyBMKG/)
[![python](https://img.shields.io/pypi/pyversions/PyBMKG.svg)](https://pypi.org/project/PyBMKG/)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/license/mit/)

This is documentation for the `PyBMKG` project that
is an asynchronous api wrapper written in Python for
[open data](https://data.bmkg.go.id/) on weather
forecasts and latest earthquakes in Indonesia served
by Meteorology, Climatology and Geophysics Agency
([BMKG](https://bmkg.go.id/)).

PyBMKG was created as a wrapper to handle API requests
BMKG open data asynchronously. This is because the
available API does not follow API standards in general,
therefore a wrapper was created which is expected to
make it easier to use the BMKG open data API with Python.

We use the third party library [aiohttp](https://docs.aiohttp.org/en/stable/)
for asynchronous client requests and it has been tested
to work well using the [asyncio](https://docs.python.org/3/library/asyncio.html)
library. Also it use [dataclass](https://docs.python.org/3/library/dataclasses.html)
as the schema.

## Docs

You can start reading the documentation [here](https://pybmkg.readthedocs.io/en/latest/).

## Contributing

Glad to hear you want to contribute to PyBMKG. Please see
[contributing guidelines](https://pybmkg.readthedocs.io/en/latest/how-to-guides/#contributing).

## Acknowledgements

We would like to thank the Meteorology, Climatology
and Geophysics Agency (BMKG) for its [open data service](https://data.bmkg.go.id/)
on weather forecasts and latest earthquake information.
