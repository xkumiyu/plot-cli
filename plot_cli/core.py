from typing import Callable, Optional

import click
import matplotlib.pyplot as plt
import pandas as pd

from . import __version__


def common_options(f: Callable) -> Callable:
    """Set common options."""
    f = click.option("--title", help="Figure title.")(f)
    f = click.option("--index_col", type=click.IntRange(0), help="index column.")(f)
    f = click.option(
        "--header",
        type=click.IntRange(-1),
        default=0,
        show_default=True,
        help="Number of lines used as header. If -1, no header.",
    )(f)
    f = click.option(
        "-o",
        "--output",
        "out_file",
        type=click.Path(dir_okay=False, writable=True),
        help="Path of output file.",
    )(f)
    f = click.option(
        "-i",
        "--input",
        "in_file",
        type=click.Path(exists=True, dir_okay=False),
        help="Path of input file.",
    )(f)
    return f


@click.group(invoke_without_command=True)
@common_options
@click.version_option(
    version=click.style(__version__, fg="cyan"), message="%(prog)s version %(version)s"
)
@click.pass_context
def cli(
    ctx,
    **kwargs
    # xlabel: str,
    # ylabel: str,
) -> None:
    """Command Line Interface for Data Visualization."""
    if ctx.invoked_subcommand is None:
        _plot(**kwargs)


@cli.command()
@common_options
def line(**kwargs) -> None:
    """Plot 2D line graph."""
    _plot(**kwargs)


@cli.command()
@common_options
def bar(**kwargs) -> None:
    """Plot bar graph."""
    _plot(params={"kind": "bar", "rot": 0}, **kwargs)


@cli.command()
@common_options
def hist(**kwargs) -> None:
    """Plot histgram."""
    _plot(params={"kind": "hist"}, **kwargs)


@cli.command()
@common_options
@click.option("--x_col", default=0)
@click.option("--y_col", default=1)
def scatter(x_col: int, y_col: int, **kwargs):
    """Plot scatter."""
    _plot(params={"kind": "scatter", "x": x_col, "y": y_col}, **kwargs)


@cli.command()
@common_options
@click.option("--y_col", default=0)
def pie(y_col, **kwargs) -> None:
    """Plot pie chart."""
    _plot(params={"kind": "pie", "y": y_col}, **kwargs)


def _plot(
    in_file: Optional[str],
    out_file: Optional[str],
    header: int,
    index_col: Optional[int],
    title: Optional[str],
    params: dict = {},
) -> None:
    fig, ax = plt.subplots()

    data = read_data(in_file, header, index_col)
    data.plot(ax=ax, **params)

    if title:
        ax.set_title(title)

    if out_file:
        fig.savefig(out_file)
    else:
        plt.show()


def read_data(
    in_file: Optional[str], header: int, index_col: Optional[int]
) -> pd.DataFrame:
    """Read data from file or stdin."""
    stdin_text = click.get_text_stream("stdin")
    if not stdin_text.isatty():
        fp = stdin_text
    else:
        if in_file is None:
            raise click.UsageError('If you do not use pipes, "-i" option is required.')
        fp = open(in_file)

    if header == -1:
        df = pd.read_csv(fp, index_col=index_col)
    else:
        df = pd.read_csv(fp, header=header, index_col=index_col)

    return df
