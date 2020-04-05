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

### Available Graph Types

Subcommands allow you to use a variety of graphs.

| subcommand | graph types |
| :-- | :-- |
| line | Line graph |
| bar | Vertical bar graph |
| barh | Horizontal bar graph |
| area | Area plot |
| box | Box plot |
| hist | Histogram |
| scatter | Scatter plot |
| pie | Pie chart |

### Examples

```sh
echo "0\n1\n4" | plot
```

![example](https://user-images.githubusercontent.com/6437204/78469450-6ac1be00-775c-11ea-853f-e676c7784544.png)

## Line Graph

### Basic Line

```csv
1
3
2
```

```sh
plot line -i data.csv
```

![Basic Line](https://user-images.githubusercontent.com/6437204/78469479-9f357a00-775c-11ea-81e6-41ce3ee8a4c7.png)

### with Header

```csv
x
1
3
2
```

```sh
plot line -i data.csv --header
```

![Basic Line with Header](https://user-images.githubusercontent.com/6437204/78469555-43b7bc00-775d-11ea-9ab9-83761b2a8944.png)

### Set Title, Label and Legend

```sh
plot line -i data.csv --title "Basic Line" --x-label x --y-label y --legends line
```

![Basic Line with Title and Label](https://user-images.githubusercontent.com/6437204/78469531-1408b400-775d-11ea-9863-814f2a6b13ff.png)

### Multiple Lines

```csv
year,blue,red
1990,20,4
1997,18,25
2003,489,281
2009,675,600
2014,1776,1900
```

```sh
plot line -i data.csv --header --index-col 0
```

```sh
plot line -i data.csv --header --index-col year
```

![Multiple Lines](https://user-images.githubusercontent.com/6437204/78469581-82e60d00-775d-11ea-9e6e-58ede68c41d1.png)

## Bar Graph

### Basic Bar

```csv
1
3
2
```

```sh
plot bar -i data.csv
```

![Basic Bar](https://user-images.githubusercontent.com/6437204/78469595-ac9f3400-775d-11ea-95a9-6d861ab5452e.png)

## Area Plot

```sh
plot area -i data.csv
```

![Area Plot](https://user-images.githubusercontent.com/6437204/78470202-84fe9a80-7762-11ea-80b3-77755ffab0fa.png)

## Box Plot

```sh
plot box -i data.csv
```

![Box Plot](https://user-images.githubusercontent.com/6437204/78470219-a9f30d80-7762-11ea-8a2c-655fc2c58b91.png)

## Histogram

```sh
plot hist -i data.csv
```

## Scatter plot

```sh
plot scatter -i data.csv
```

## Pie chart

```sh
plot pie -i data.csv
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
