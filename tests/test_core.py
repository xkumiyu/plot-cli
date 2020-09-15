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
    assert re.match(r"^\w+ version \d+.\d+.\d+(\.?(a|b|rc|dev)\d+)?$", result.output)


def test_plot_and_save(tmp_path, runner):
    path = tmp_path / "plot.png"

    assert path.exists() is False

    result = runner.invoke(cli, ["-o", str(path)], input="0,0\n1,1")

    assert result.exit_code == 0
    assert result.output == ""
    assert path.exists() is True


@pytest.mark.parametrize(
    "kind", ["line", "bar", "barh", "area", "box", "hist", "scatter", "pie"]
)
def test_plot(tmp_path, runner, kind):
    path = tmp_path / "plot.png"

    assert path.exists() is False

    result = runner.invoke(cli, [kind, "-o", str(path)], input="0,0\n1,1")

    assert result.exit_code == 0
    assert result.output == ""
    assert path.exists() is True


@pytest.mark.parametrize(
    "option",
    [
        ["--title", "title"],
        ["--x-label", "x"],
        ["--y-label", "y"],
        ["--columns", "x,y"],
        ["--use-cols", "0"],
    ],
)
def test_with_option(tmp_path, runner, option):
    path = tmp_path / "plot.png"

    assert path.exists() is False

    args = option + ["-o", str(path)]
    result = runner.invoke(cli, args, input="0,0\n1,1")

    assert result.exit_code == 0
    assert result.output == ""
    assert path.exists() is True
