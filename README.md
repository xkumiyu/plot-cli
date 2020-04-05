# Plot CLI

Plot CLI is command line interface for data visualization.

[![PyPi][pypi-version]][pypi] [![Python Version][python-version]][pypi] [![GitHub Workflow Status][actions-status]][actions] [![codecov][codecov-status]][codecov] [![License][license]][license-file]

It works on Python 3.6.1 and greater.

## Installation

Install using pip:

```sh
pip install plot-cli
```

## Usage

To plot from file, use "-i" option:

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

See also `plot --help`.

### Examples

```sh
echo "0\n1\n4" | plot
```

## Shell Complete

The plot-cli supports Shell completion.

For Bash, add this to `~/.bashrc`:

```sh
eval "$(_PLOT_COMPLETE=source plot)"
```

For Zsh, add this to `~/.zshrc`:

```sh
eval "$(_PLOT_COMPLETE=source_zsh plot)"
```

For Fish, add this to `~/.config/fish/completions/plot-cli.fish`:

```sh
eval (env _PLOT_COMPLETE=source_fish plot)
```

## Change Log

See [Change Log](CHANGELOG.md).

[pypi]: https://pypi.org/project/plot-cli
[pypi-version]: https://img.shields.io/pypi/v/plot-cli
[python-version]: https://img.shields.io/pypi/pyversions/plot-cli
[actions]: https://github.com/xkumiyu/plot-cli/actions
[actions-status]: https://img.shields.io/github/workflow/status/xkumiyu/plot-cli/Python%20package
[codecov]: https://codecov.io/gh/xkumiyu/plot-cli
[codecov-status]: https://img.shields.io/codecov/c/github/xkumiyu/plot-cli
[license]: https://img.shields.io/github/license/xkumiyu/plot-cli
[license-file]: https://github.com/xkumiyu/plot-cli/blob/master/LICENSE
