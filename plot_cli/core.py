from pathlib import Path
from tempfile import TemporaryDirectory
from time import sleep
from typing import Optional

import click
import matplotlib.pyplot as plt
import numpy as np

from . import __version__


@click.command()
@click.option(
    "-i",
    "in_file",
    type=click.Path(exists=True, dir_okay=False),
    help="Path of input file.",
)
@click.option(
    "-o",
    "out_file",
    type=click.Path(dir_okay=False, writable=True),
    help="Path of output file.",
)
@click.option(
    "--header",
    "header_index",
    type=click.IntRange(-1),
    default=0,
    show_default=True,
    help="Number of lines used as header. If -1, no header.",
)
@click.option("--title", help="Figure title.")
@click.option("--xlabel", default="x", show_default=True, help="Figure x lable.")
@click.option("--ylabel", default="y", show_default=True, help="Figure y lable.")
@click.version_option(
    version=click.style(__version__, fg="cyan"), message="%(prog)s version %(version)s"
)
def cli(
    in_file: Optional[str],
    out_file: Optional[str],
    header_index: int,
    title: Optional[str],
    xlabel: str,
    ylabel: str,
) -> None:
    """Command Line Interface for Data Visualization."""
    stdin_text = click.get_text_stream("stdin")
    if not stdin_text.isatty():
        fp = stdin_text
    else:
        if in_file is None:
            raise click.UsageError('If you do not use pipes, "-i" option is required.')
        fp = open(in_file)

    delimiter = ","

    header = None
    for _ in range(header_index + 1):
        header = next(fp).rstrip().split(delimiter)

    data = np.genfromtxt(fp, delimiter=delimiter, dtype=np.float32)
    fp.close()

    fig, ax = plt.subplots()

    if header:
        if header[0]:
            xlabel = header[0]
        if len(header) == 2:
            ylabel = header[1]
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)

    if title:
        ax.set_title(title)

    num_column = data.shape[1]
    for i in range(1, num_column):
        (line,) = ax.plot(data[:, 0], data[:, i])
        if header:
            line.set_label(header[i])
    if header:
        ax.legend()

    if out_file:
        fig.savefig(out_file)
    else:
        with TemporaryDirectory() as tmp_dir:
            tmp = Path(tmp_dir) / "plot.png"
            fig.savefig(tmp)
            click.launch(str(tmp))
            sleep(0.1)
