import functools
from enum import Enum, IntEnum, unique


@unique
class Color(IntEnum):
    """
    Basic colors
    """

    BLACK = 0
    RED = 1
    GREEN = 2
    YELLOW = 3
    BLUE = 4
    PURPLE = 5
    CYAN = 6
    WHITE = 7

    def __str__(self):
        return str(self.value)


@unique
class Style(Enum):
    """
    Represent a terminal style.
    """

    BOLD = functools.partial(lambda t: t.bold)
    DIM = functools.partial(lambda t: t.dim)
    UNDERLINE = functools.partial(lambda t: t.smul)
    BLINK = functools.partial(lambda t: t.blink)
    STANDOUT = functools.partial(lambda t: t.smso)
    REVERSE = functools.partial(lambda t: t.rev)
    RESET = functools.partial(lambda t: t.sgr0)

    BLACK = functools.partial(lambda t: t.setaf(Color.BLACK))
    RED = functools.partial(lambda t: t.setaf(Color.RED))
    GREEN = functools.partial(lambda t: t.setaf(Color.GREEN))
    YELLOW = functools.partial(lambda t: t.setaf(Color.YELLOW))
    BLUE = functools.partial(lambda t: t.setaf(Color.BLUE))
    PURPLE = functools.partial(lambda t: t.setaf(Color.PURPLE))
    CYAN = functools.partial(lambda t: t.setaf(Color.CYAN))
    WHITE = functools.partial(lambda t: t.setaf(Color.WHITE))

    BG_BLACK = functools.partial(lambda t: t.setab(Color.BLACK))
    BG_RED = functools.partial(lambda t: t.setab(Color.RED))
    BG_GREEN = functools.partial(lambda t: t.setab(Color.GREEN))
    BG_YELLOW = functools.partial(lambda t: t.setab(Color.YELLOW))
    BG_BLUE = functools.partial(lambda t: t.setab(Color.BLUE))
    BG_PURPLE = functools.partial(lambda t: t.setab(Color.PURPLE))
    BG_CYAN = functools.partial(lambda t: t.setab(Color.CYAN))
    BG_WHITE = functools.partial(lambda t: t.setab(Color.WHITE))
