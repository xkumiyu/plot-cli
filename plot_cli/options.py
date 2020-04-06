from typing import Any, Callable, Optional

import click
import matplotlib.pyplot as plt

from .config import config


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


def _header_option(f: Callable) -> Callable:
    def callback(ctx: click.Context, param: Any, value: bool) -> Optional[int]:
        value = config.header or value
        if value:
            return 0
        else:
            return None

    return click.option(
        "--header", is_flag=True, callback=callback, help="Use first row as header."
    )(f)


def _style_option(f: Callable) -> Callable:
    def callback(ctx: click.Context, param: Any, value: tuple) -> tuple:
        value = value or config.styles
        value = tuple(set(value))
        return value

    return click.option(
        "--style",
        "style_list",
        type=click.Choice(plt.style.available + ["xkcd"]),
        multiple=True,
        help="Use style settings.",
        callback=callback,
    )(f)


def common_options(f: Callable) -> Callable:
    """Set common options."""
    f = _style_option(f)
    f = click.option("--grid", "show_grid", is_flag=True, help="Show the grid.")(f)
    f = click.option("--no-legend", is_flag=True, help="Hides the legend.")(f)
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
    f = _header_option(f)
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
