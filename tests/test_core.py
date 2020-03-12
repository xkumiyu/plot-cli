import re

import pytest
from click.testing import CliRunner

from plot_cli.core import cli


@pytest.fixture
def runner():
    yield CliRunner()


def test_show_version(runner):
    result = runner.invoke(cli, ["--version"])

    assert result.exit_code == 0
    assert re.match(r"^\w+ version \d+.\d+.\d+([a|b|rc]\d+)?$", result.output)


def test_plot_and_save(tmp_path, runner):
    path = tmp_path / "plot.png"

    assert path.exists() is False

    result = runner.invoke(cli, ["-o", str(path)], input="x,y\n1,1\n2,4")

    assert result.exit_code == 0
    assert result.output == ""
    assert path.exists() is True


@pytest.mark.parametrize("kind", ["line", "bar", "hist", "scatter", "pie"])
def test_plot(tmp_path, runner, kind):
    path = tmp_path / "plot.png"

    assert path.exists() is False

    result = runner.invoke(cli, [kind, "-o", str(path)], input="x,y\n1,1\n2,4")

    assert result.exit_code == 0
    assert result.output == ""
    assert path.exists() is True
