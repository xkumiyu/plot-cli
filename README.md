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

To use tsv file:

```sh
plot -i data.tsv --delimiter '\t'
```

To change [style](https://matplotlib.org/gallery/style_sheets/style_sheets_reference.html):

```sh
plot --style ggplot
```

See also `plot --help`.

### Available Graph Types

Subcommands allow you to use a variety of graphs.

| subcommand | graph type |
| :-- | :-- |
| line | Line graph |
| bar | Bar graph |
| area | Area plot |
| box | Box plot |
| hist | Histogram |
| scatter | Scatter plot |
| pie | Pie chart |

## Line Graph

### Basic Line

```csv
1
3
2
```

```sh
plot line -i simple.csv
```

![basic-line](https://user-images.githubusercontent.com/6437204/78481527-cdc54c00-7780-11ea-98b2-370c8c4ae702.png)

### with Header

```csv
x
1
3
2
```

```sh
plot line -i simple-with-header.csv --header
```

![Basic Line with Header](https://user-images.githubusercontent.com/6437204/78469555-43b7bc00-775d-11ea-9ab9-83761b2a8944.png)

### Set Title, Label and Legend

```sh
plot line -i simple.csv --title "Basic Line" --x-label x --y-label y --legends line
```

![Basic Line with Title and Label](https://user-images.githubusercontent.com/6437204/78469531-1408b400-775d-11ea-9863-814f2a6b13ff.png)

### Change line style

```sh
plot line -i simple.csv --marker o --linestyle dashed
```

![basic-line-changed-style](https://user-images.githubusercontent.com/6437204/78501898-03762f00-7799-11ea-8cf6-473389ee3313.png)

### Multiple Lines

```csv
year,a,b
1990,20,4
1997,18,25
2003,489,281
2009,675,600
2014,1776,1900
```

```sh
plot line -i multiple.csv --header --index-col 0
```

```sh
plot line -i multiple.csv --header --index-col year
```

![multiple-lines](https://user-images.githubusercontent.com/6437204/78489195-f0586480-7782-11ea-9160-0cbee89ccaf1.png)

## Bar Graph

### Vertical Bar

```sh
plot bar -i random.csv --header
```

![vertical-bar](https://user-images.githubusercontent.com/6437204/78498634-6ca07700-7786-11ea-8ff0-4dbf9c273c3b.png)

### Horizontal Bar

```sh
plot bar -i random.csv --header --horizontal
```

![horizontal-bar](https://user-images.githubusercontent.com/6437204/78498666-90fc5380-7786-11ea-8fda-69422227290b.png)

### Stacked Bar

```sh
plot bar -i random.csv --header --stacked
```

![stacked-bar](https://user-images.githubusercontent.com/6437204/78498807-6f4f9c00-7787-11ea-8b48-53f4ad19a889.png)

## Histogram

### Basic Histogram

```sh
plot hist -i uniform.csv --header --use-cols 0 --no-legend
```

![basic-hist](https://user-images.githubusercontent.com/6437204/78499145-fbfb5980-7789-11ea-84e1-8192b7493384.png)

### Multiple Histogram

```sh
plot hist -i uniform.csv --header --alpha 0.5
```

![multiple-hist](https://user-images.githubusercontent.com/6437204/78499522-1f270880-778c-11ea-8dd5-a49f411e54d4.png)

## Box Plot

```sh
plot box -i random.csv --header
```

![box-plot](https://user-images.githubusercontent.com/6437204/78500061-5d71f700-778f-11ea-9c8e-ff44600ba38f.png)

## Area Plot

```sh
plot area -i random.csv --header
```

![area-plot](https://user-images.githubusercontent.com/6437204/78500345-d160cf00-7790-11ea-9faf-f1429253736d.png)

## Scatter plot

```sh
plot scatter -i random.csv --header
```

![scatter](https://user-images.githubusercontent.com/6437204/78500349-d4f45600-7790-11ea-9c30-4081942a19b9.png)

## Pie chart

```sh
plot pie -i with-index.csv --index-col 0 --header
```

![pie-chart](https://user-images.githubusercontent.com/6437204/78500945-6b764680-7794-11ea-9451-3c17a9b07416.png)

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
