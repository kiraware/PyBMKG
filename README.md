# PyBMKG

![CI](https://github.com/kiraware/PyBMKG/actions/workflows/ci.yml/badge.svg)
[![Docs](https://readthedocs.org/projects/pybmkg/badge/?version=latest)](https://pybmkg.readthedocs.io/en/latest/?badge=latest)
[![codecov](https://codecov.io/gh/kiraware/PyBMKG/graph/badge.svg?token=MN6AXAHO0P)](https://codecov.io/gh/kiraware/PyBMKG)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)
[![security: bandit](https://img.shields.io/badge/security-bandit-yellow.svg)](https://github.com/PyCQA/bandit)
[![Checked with mypy](http://www.mypy-lang.org/static/mypy_badge.svg)](http://mypy-lang.org/)
[![Ruff](https://camo.githubusercontent.com/7f995d42c2de5a9eb8ced2df552a0813050d324427a3facabfcfa5f88cb11c59/68747470733a2f2f696d672e736869656c64732e696f2f656e64706f696e743f75726c3d68747470733a2f2f7261772e67697468756275736572636f6e74656e742e636f6d2f636861726c6965726d617273682f727566662f6d61696e2f6173736574732f62616467652f76312e6a736f6e)](https://github.com/astral-sh/ruff)
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
