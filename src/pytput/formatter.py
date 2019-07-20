import os
import sys
from string import Formatter

from pytput.style import Style
from pytput.tput import Tput

__PYTPUT_DISABLED = "PYTPUT_DISABLE"


def pytput_is_enabled(check_tty=True):
    return not os.getenv(__PYTPUT_DISABLED) and (not check_tty or sys.stdout.isatty())


class TputFormatter(Formatter):
    """
    Formatter to format a string using styles
    """

    def __init__(self, check_tty=True):
        self.__check_tty = check_tty
        self.__tput = Tput()

    def format_field(self, value, format_spec):
        # Do formatting
        before = ""
        super_format = []
        for item in format_spec.split(","):
            # Ensure style is not already set
            if item.upper() in Style.__members__:
                # Check termicolor is enabled
                if pytput_is_enabled(self.__check_tty):
                    s = Style[item.upper()]
                    before += s.value(self.__tput)
            else:
                super_format.append(item)
        # Perform super() formatting
        value = super().format_field(value, ",".join(super_format))
        # Check if no formatting found
        if len(before) == 0:
            return value
        # Return formatted value
        return before + value + self.__tput.sgr0
