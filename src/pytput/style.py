from dataclasses import dataclass
from enum import IntEnum, unique
from functools import partial

from pytput.tput import Tput


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


@dataclass
class TputStyle:
    _func: callable

    def __str__(self):
        return self.value

    @property
    def value(self):
        return self._func()

    def apply(self, text: str):
        return self.value + str(text) + Style.RESET.value


class Style:
    """
    Represent a terminal style.
    """

    BOLD = TputStyle(Tput.bold)
    DIM = TputStyle(Tput.dim)
    UNDERLINE = TputStyle(Tput.smul)
    BLINK = TputStyle(Tput.blink)
    STANDOUT = TputStyle(Tput.smso)
    REVERSE = TputStyle(Tput.rev)
    RESET = TputStyle(Tput.sgr0)

    BLACK = TputStyle(partial(Tput.setaf, Color.BLACK))
    RED = TputStyle(partial(Tput.setaf, Color.RED))
    GREEN = TputStyle(partial(Tput.setaf, Color.GREEN))
    YELLOW = TputStyle(partial(Tput.setaf, Color.YELLOW))
    BLUE = TputStyle(partial(Tput.setaf, Color.BLUE))
    PURPLE = TputStyle(partial(Tput.setaf, Color.PURPLE))
    CYAN = TputStyle(partial(Tput.setaf, Color.CYAN))
    WHITE = TputStyle(partial(Tput.setaf, Color.WHITE))

    BG_BLACK = TputStyle(partial(Tput.setab, Color.BLACK))
    BG_RED = TputStyle(partial(Tput.setab, Color.RED))
    BG_GREEN = TputStyle(partial(Tput.setab, Color.GREEN))
    BG_YELLOW = TputStyle(partial(Tput.setab, Color.YELLOW))
    BG_BLUE = TputStyle(partial(Tput.setab, Color.BLUE))
    BG_PURPLE = TputStyle(partial(Tput.setab, Color.PURPLE))
    BG_CYAN = TputStyle(partial(Tput.setab, Color.CYAN))
    BG_WHITE = TputStyle(partial(Tput.setab, Color.WHITE))

    @classmethod
    def all_styles(cls):
        return tuple(
            sorted(n for n, o in cls.__dict__.items() if isinstance(o, TputStyle))
        )

    @classmethod
    def find(cls, name: str):
        for n, o in cls.__dict__.items():
            if isinstance(o, TputStyle) and n.lower() == name.lower():
                return o
