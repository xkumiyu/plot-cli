# Plot CLI

[![GitHub Workflow Status][actions-status]][actions] [![codecov][codecov-status]][codecov] [![License][license]][license-file]

Command Line Interface for Data Visualization.

The plot-cli works on Python versions:

- Python 3.6
- Python 3.7
- Python 3.8

## Installation

Install and update using pip:

```sh
pip install plot-cli
```

## Usage

To plot from CSV file, use "-i" option:

```sh
plot -i data.csv
```

To plot from stdin:

```sh
cat data.csv | plot
```

To save to file, use "-o" option:

```sh
plot -i data.csv -o plot.png
```

If you do not use "-o" option, it is saved in a temporary file and opened.

### Example

```sh
echo "x,y\n1,1\n2,4" | plot
```

## Change Log

See [Change Log](CHANGELOG.md).

[actions]: https://github.com/xkumiyu/plot-cli/actions
[actions-status]: https://img.shields.io/github/workflow/status/xkumiyu/plot-cli/Python%20package
[codecov]: https://codecov.io/gh/xkumiyu/plot-cli
[codecov-status]: https://img.shields.io/codecov/c/github/xkumiyu/plot-cli
[license]: https://img.shields.io/github/license/xkumiyu/plot-cli
[license-file]: https://github.com/xkumiyu/plot-cli/blob/master/LICENSE
