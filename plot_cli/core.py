from typing import IO, Optional

import click
import matplotlib.pyplot as plt
import pandas as pd

from . import __version__
from .options import common_options


@click.group(invoke_without_command=True)
@common_options
@click.version_option(
    version=click.style(__version__, fg="cyan"), message="%(prog)s version %(version)s"
)
@click.pass_context
def cli(ctx, **kwargs) -> None:
    """Command Line Interface for Data Visualization."""
    if ctx.invoked_subcommand is None:
        _plot(**kwargs)


@cli.command()
@common_options
@click.option(
    "--marker",
    help="The marker style to use.",
)
@click.option(
    "--linestyle",
    "--ls",
    type=click.Choice(
        ["-", "--", "-.", ":", "solid", "dashed", "dashdot", "dotted", "none"]
    ),
    help="The line style to use.",
)
def line(marker: str, linestyle: str, **kwargs) -> None:
    """Plot 2D line graph."""
    _plot(params={"marker": marker, "linestyle": linestyle}, **kwargs)


@cli.command()
@common_options
@click.option("--horizontal", is_flag=True, help="Make the graph horizontal.")
@click.option("--stacked", is_flag=True, help="Stacked flag.")
def bar(horizontal: bool, stacked: bool, **kwargs) -> None:
    """Plot bar graph."""
    if horizontal:
        _plot(params={"kind": "barh", "rot": 0, "stacked": stacked}, **kwargs)
    else:
        _plot(params={"kind": "bar", "rot": 0, "stacked": stacked}, **kwargs)


@cli.command()
@common_options
@click.option("--stacked", is_flag=True, help="Stacked flag.")
def barh(stacked: bool, **kwargs) -> None:
    """Plot horizontal bar graph."""
    _plot(params={"kind": "barh", "rot": 0, "stacked": stacked}, **kwargs)


@cli.command()
@common_options
def area(**kwargs) -> None:
    """Plot area plot."""
    _plot(params={"kind": "area"}, **kwargs)


@cli.command()
@common_options
def box(**kwargs) -> None:
    """Plot box plot."""
    _plot(params={"kind": "box"}, **kwargs)


@cli.command()
@common_options
@click.option(
    "--alpha",
    type=click.FloatRange(0, 1),
    help="The value of the alpha channel that represents the graph transparency.",
)
@click.option(
    "--bins", type=int, default=10, help="Number of histogram bins to be used."
)
def hist(alpha: float, bins: int, **kwargs) -> None:
    """Plot histgram."""
    _plot(params={"kind": "hist", "alpha": alpha, "bins": bins}, **kwargs)


@cli.command()
@common_options
@click.option(
    "--x-col",
    default=0,
    show_default=True,
    help="Position of the column used for x-axis.",
)
@click.option(
    "--y-col",
    default=1,
    show_default=True,
    help="Position of the column used for y-axis.",
)
def scatter(x_col: int, y_col: int, **kwargs):
    """Plot scatter."""
    _plot(params={"kind": "scatter", "x": x_col, "y": y_col}, **kwargs)


@cli.command()
@common_options
@click.option(
    "--y-col", default=0, show_default=True, help="Position of the column to plot."
)
def pie(y_col, **kwargs) -> None:
    """Plot pie chart."""
    _plot(params={"kind": "pie", "y": y_col}, **kwargs)


def _plot(
    in_file: Optional[str],
    out_file: Optional[str],
    delimiter: str,
    title: Optional[str],
    x_label: Optional[str],
    y_label: Optional[str],
    header: Optional[int],
    index_col: Optional[int],
    use_cols: Optional[list],
    no_legend: bool,
    columns: Optional[list],
    style_list: tuple,
    show_grid: bool,
    params: Optional[dict] = None,
) -> None:
    if params is None:
        params = {}
    for style in style_list:
        if style == "xkcd":
            plt.xkcd()
        else:
            plt.style.use(style)

    fig, ax = plt.subplots()

    buffer = _get_file_hander(in_file)
    data = pd.read_csv(
        buffer,
        header=header,
        index_col=index_col,
        delimiter=delimiter,
        usecols=use_cols,
        engine="python",
    )

    if columns:
        if len(columns) == len(data.columns):
            data.columns = columns
        else:
            raise click.BadParameter("Invalid columns length.")
    if no_legend or (columns is None and header is None):
        params["legend"] = False

    try:
        data.plot(ax=ax, **params)
    except TypeError as e:
        raise click.ClickException(str(e))

    if title:
        ax.set_title(title)
    if x_label:
        ax.set_xlabel(x_label)
    if y_label:
        ax.set_ylabel(y_label)
    if show_grid:
        ax.grid()

    if out_file:
        fig.savefig(out_file)
    else:
        plt.show()


def _get_file_hander(in_file: Optional[str]) -> IO[str]:
    stdin_text = click.get_text_stream("stdin")
    if not stdin_text.isatty():
        buffer = stdin_text
    else:
        if in_file is None:
            raise click.UsageError('If you do not use pipes, "-i" option is required.')
        buffer = open(in_file)
    return buffer
