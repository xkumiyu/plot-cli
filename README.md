# Plot CLI

Plot CLI is command line interface for data visualization.

[![PyPi][pypi-version]][pypi] [![Python Version][python-version]][pypi] [![GitHub Workflow Status][actions-status]][actions] [![Documentation][docs-status]][docs] [![codecov][codecov-status]][codecov] [![License][license]][license-file]

It works on Python 3.6.1 and greater.

## Installation

Install using pip:

```sh
pip install plot-cli
```

## Getting Started

You can output a graph from stdin or a file.

```sh
cat data.csv | plot line --header --index-col year
```

![example](https://user-images.githubusercontent.com/6437204/78489195-f0586480-7782-11ea-9160-0cbee89ccaf1.png)

See the [documentation](https://plot-cli.readthedocs.io/) for detailed usage and examples.

## Change Log

See [Change Log](CHANGELOG.rst).

[pypi]: https://pypi.org/project/plot-cli
[pypi-version]: https://img.shields.io/pypi/v/plot-cli
[python-version]: https://img.shields.io/pypi/pyversions/plot-cli
[actions]: https://github.com/xkumiyu/plot-cli/actions
[actions-status]: https://img.shields.io/github/workflow/status/xkumiyu/plot-cli/Python%20package
[docs]: https://plot-cli.readthedocs.io/
[docs-status]: https://img.shields.io/readthedocs/plot-cli/latest
[codecov]: https://codecov.io/gh/xkumiyu/plot-cli
[codecov-status]: https://img.shields.io/codecov/c/github/xkumiyu/plot-cli
[license]: https://img.shields.io/github/license/xkumiyu/plot-cli
[license-file]: https://github.com/xkumiyu/plot-cli/blob/master/LICENSE
