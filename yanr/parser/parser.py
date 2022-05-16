import functools

from yanr.base.base import Base
from yanr.base.base import click_options as base_options


class Parser(Base):
    def __init__(self, source, destination):
        """Base class for parsers

        Args:
            source (str or dict or None): url/path, dict or None
            destination (str or dict or None): url/path, dict or None

        Returns: dict or None
        """
        super().__init__(source=source, destination=destination)


def click_options(func):
    @base_options
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    return wrapper
