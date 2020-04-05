from typing import IO, Callable, Optional

import click
import matplotlib.pyplot as plt
import pandas as pd

from . import __version__


def _columns_callback(ctx, param, value):
    if value is None:
        return None
    else:
        return value.split(",")


def _validate_use_cols(ctx, param, value):
    if value is None:
        return None
    try:
        return set([int(x) for x in value.split(",")])
    except ValueError as e:
        raise click.BadParameter(e)


def _validate_index_col(ctx, param, value):
    if value is not None and value.replace("-", "").isnumeric():
        x = int(value)
        if x < 0:
            raise click.BadParameter(f"{x} is smaller than the minimum valid value 0")
        else:
            return x
    else:
        return value


def _header_callback(ctx, param, value):
    if value:
        return 0
    else:
        return None


def common_options(f: Callable) -> Callable:
    """Set common options."""
    f = click.option(
        "--style",
        "style_list",
        type=click.Choice(plt.style.available + ["xkcd"]),
        multiple=True,
        help="Use style settings.",
    )(f)
    f = click.option(
        "--columns",
        "--legends",
        callback=_columns_callback,
        help=(
            "List of column names to use. "
            'To set more than one, do the follows. --columns "x,y"'
        ),
    )(f)
    f = click.option(
        "--use-cols",
        callback=_validate_use_cols,
        help=(
            "List of position of the column to use. "
            'To set more than one, do the follows. --use-cols "0,1"'
        ),
    )(f)
    f = click.option(
        "--index-col",
        callback=_validate_index_col,
        help="Position or name of the column used as index.",
    )(f)
    f = click.option(
        "--header",
        is_flag=True,
        callback=_header_callback,
        help="Use first row as header.",
    )(f)
    f = click.option("--x-label", help="X-axis label.")(f)
    f = click.option("--y-label", help="Y-axis label.")(f)
    f = click.option("--title", help="Figure title.")(f)
    f = click.option("--delimiter", default=",", help="Delimiter to use.")(f)
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
def cli(ctx, **kwargs) -> None:
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
    columns: Optional[list],
    style_list: tuple,
    params: dict = {},
) -> None:
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
    if columns is None and header is None:
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
