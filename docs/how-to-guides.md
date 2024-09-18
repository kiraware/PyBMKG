# How-To Guides

## Contributing

Thank you for your interest in contributing to PyBMKG!
We welcome contributions from everyone. Before you get
started, please take a moment to review the following
guidelines.

### Code of Conduct

Please note that this project adheres to the Contributor
Covenant Code of Conduct. By participating, you are
expected to uphold this code. Please report any
unacceptable behavior.

### Ways to Contribute

Here are a few ways you can contribute to PyBMKG:

- Reporting bugs
- Suggesting new features
- Writing or improving documentation
- Submitting bug fixes or enhancements via Pull Requests

### Getting Started

You can contribute directly to PyBMKG by submit a pull
request. We encourage linear history on commit. The
project uses Squash-and-Merge strategy for GitHub Merge
button.

Basically it means that there is no need to rebase a Pull
Request against main branch. Just git merge main into your
working copy (a fork) if needed. The Pull Request is
automatically squashed into the single commit once the PR
is accepted.

The pull request submitted must be very specific so that
one pull request specifically describes one change.

First clone the forked repository with the
following command

```console
git clone https://github.com/YOUR-USERNAME/PyBMKG
```

Then create a branch for pull requests in the fork
repository with a short branch name that explains in
general what pull request will be submitted. For
example in the following command

```console
git branch fix-docs-typos
```

And don't forget to switch and start making changes
from there.

```console
git switch fix-docs-typos
```

After that, make sure your terminal's working directory
is active in the PyBMKG folder and [pre-commit](https://pre-commit.com/)
is installed globally. Then to install pre-commit git
hook use the following command

```console
pre-commit install
```

We use [Poetry](https://python-poetry.org/) as the project
packaging and dependency management. Install development
dependency with the following command

```console
poetry install
```

And done! You can make your changes and test thoroughly.
Then push your branch to your fork and submit a pull request.

!!! tip
    If you have installed [poethepoet](https://poethepoet.natn.io/index.html)
    globally, then you can use the command below only with
    `poe lint`, `poe format`, etc instead of `poetry run poe lint`,
    `poetry run poe format`, etc.

### Linting

We use [Ruff](https://docs.astral.sh/ruff/) as a linter,
[mypy](https://mypy.readthedocs.io/en/stable/) as a static type
checker, and [Bandit](https://bandit.readthedocs.io/en/latest/)
for find common security issues in Python code. To run the Ruff,
mypy and Bandit linter together you can use the following command

```console
poetry run poe lint
```

Or if you want to do it one by one you can use the following command

```console
poetry run poe ruff
poetry run poe mypy
poetry run poe bandit
```

For fix lint with ruff, run

```console
poetry run poe ruff-fix
```

### Formatting

We use [Ruff](https://docs.astral.sh/ruff/) also as a formatter.
To run Ruff formatter you can use the following command

```console
poetry run poe format
```

If you want to check only, use

```console
poetry run poe format-check
```

### Testing

We use [pytest](https://docs.pytest.org/en/stable/) for testing.
To run pytest you can use the following command

```console
poetry run poe test
```

To pass more argument to pytest, use like the following example

```console
poetry run poe test --cov-report=html
```

We really pay attention to testing coverage, therefore to
contribute we are expected to make tests and if possible increase
the code coverage.

### Documenting

We use [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)
as static site documentation with markdown. PyBMKG does not include
docs dependencies by default, to install it you can use the
following command

```console
poetry install --with docs
```

Documentation is very important to make it easier for users to use
a library. So writing documentation for changes to contributed code
is very important. To run development mode you can use the following
command

```console
poetry run poe docs-serve
```

And to build the documentation use the following command

```console
poetry run poe docs-build
```

### Releasing

We use the GitHub workflow to automatically release to PyPI when we
release to GitHub. The special environment for people who have access
to the workflow is in the GitHub environment with the name `production`.
Each release tag must be the same as `version` in `pyproject.toml` in
the `tool.poetry` section.

### Update Dependency

We use GitHub dependabot to automatically update dependency and GitHub
action. To update the dependency in pre-commit, you can use command

```console
pre-commit autoupdate
```

### License

By contributing to PyBMKG, you agree that your contributions will be
licensed under the project's [MIT License](https://github.com/kiraware/PyBMKG/blob/main/LICENSE).
