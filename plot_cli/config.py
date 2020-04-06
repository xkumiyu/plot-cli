from configparser import ConfigParser, SectionProxy
from distutils.util import strtobool
from pathlib import Path


class Config(object):
    """Manage config.

    Use the config file placed in ~.plot-cli/config.

    Note:
        You can write a config like the following.

        [settings]
        style = Solarize_Light2
        header = true
    """

    def __init__(self) -> None:
        parser = ConfigParser()

        path = Path.home() / Path(".plot-cli/config")
        if path.exists():
            parser.read(path)

        self.settings = SectionProxy(parser, "settings")

    @property
    def header(self) -> bool:
        """Get header."""
        value = self.settings.get("header")
        if value:
            # TODO: check value
            return bool(strtobool(value))
        return False

    @property
    def styles(self) -> tuple:
        """Get styles."""
        value = self.settings.get("style")
        if value:
            # TODO: check value
            return tuple(value.replace(" ", "").split(","))
        return ()


config = Config()
