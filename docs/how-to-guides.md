# How-To Guides

## Contributing

### Getting Started

You can contribute directly to PyBMKG by submit a pull
request. First clone the repository with the following
command:

```console
git clone https://github.com/kiraware/PyBMKG
```

After that, make sure your terminal's working directory
is active in the PyBMKG folder. Then to install
[pre-commit](https://pre-commit.com/) git hook use the
following command:

```console
pre-commit install
```

We use [Poetry](https://python-poetry.org/) as the project
packaging and dependency management. Install development
dependency with the following command:

```console
poetry install
```

And done! You can contribute directly by getting your hands wet.

### Linting

We use [Ruff](https://docs.astral.sh/ruff/) as a linter,
[mypy](https://mypy.readthedocs.io/en/stable/) as a static type
checker, and [Bandit](https://bandit.readthedocs.io/en/latest/)
for find common security issues in Python code. To run the Ruff,
mypy and Bandit linter together you can use the following command:

```console
poetry run poe lint
```

Or if you want to do it one by one you can use the following command:

```console
poetry run poe ruff
poetry run poe mypy
poetry run poe bandit
```

### Formatting

We use [Ruff](https://docs.astral.sh/ruff/) also as a formatter.
To run Ruff formatter you can use the following command

```console
poetry run poe format
```

### Testing

We use [pytest](https://docs.pytest.org/en/stable/) for testing.
To run pytest you can use the following command:

```console
poetry run poe test
```

### Documenting

We use [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)
as static site documentation with markdown. To run development mode
you can use the following command:

```console
poetry run mkdocs serve
```
