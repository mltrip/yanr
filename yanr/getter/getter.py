import functools

from yanr.base.base import Base
from yanr.base.base import click_options as base_options


class Getter(Base):
    def __init__(self, source: str, destination: str) -> None:
        """Abstract class for getters

        Args:
            source (str): url or path to file
            destination (str): url or path to file

        Returns: None
        """
        super().__init__(source=source, destination=destination)


def click_options(func):
    @base_options
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    return wrapper