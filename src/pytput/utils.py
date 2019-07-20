from pytput.formatter import TputFormatter
from pytput.style import Style
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


def print_red(*args, **kwargs):
    """
    Builtin print-like function that print a message in red
    """
    print(Style.RED.value(_TPUT), sep="", end="")
    try:
        print(*args, **kwargs)
    finally:
        print(Style.RESET.value(_TPUT), sep="", end="")


def print_green(*args, **kwargs):
    """
    Builtin print-like function that print a message in green
    """
    print(Style.GREEN.value(_TPUT), sep="", end="")
    try:
        print(*args, **kwargs)
    finally:
        print(Style.RESET.value(_TPUT), sep="", end="")
