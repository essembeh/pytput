from pytput.formatter import TputFormatter
from pytput.style import Color
from pytput.tput import Tput


_TPUT = Tput()


def tput_format(message, *args, check_tty=True, **kwargs):
    """
    Used to format a string with keywords, use string.Formatter spec when needed
    """
    return TputFormatter(check_tty=check_tty).format(message, *args, **kwargs)


def tput_print(message, *args, **kwargs):
    """
    Format the given message with tc_format and print it
    """
    print(tput_format(message, *args, **kwargs))


def print_color(color: Color, *args, **kwargs):
    """
    Builtin print-like function that print a message in red
    """
    if isinstance(color, int):
        color = Color(color)
    elif isinstance(color, str):
        color = Color[color.upper()]
    if not isinstance(color, Color):
        raise ValueError("Unknown color: {0}".format(color))
        color = Color(color)
    print(_TPUT.setaf(color), sep="", end="")
    try:
        print(*args, **kwargs)
    finally:
        print(_TPUT.sgr0, sep="", end="")


def print_red(*args, **kwargs):
    print_color(Color.RED, *args, **kwargs)
