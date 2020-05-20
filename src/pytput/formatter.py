import sys
from string import Formatter

from pytput.style import Style
from pytput.tput import Tput


class TputFormatter(Formatter):
    """
    Formatter to format a string using styles
    """

    def __init__(self, *args, check_tty=True, **kwargs):
        Formatter.__init__(self, *args, **kwargs)
        self.check_tty = check_tty

    def format_field(self, value, format_spec):
        # Do formatting
        before = ""
        super_format = []
        for item in format_spec.split(","):
            # Ensure style is not already set
            style = Style.find(item)
            if style is not None:
                # Check pytput is enabled
                if not self.check_tty or sys.stdout.isatty():
                    before += style.value
            else:
                super_format.append(item)
        # Perform super() formatting
        value = super().format_field(value, ",".join(super_format))
        # Check if no formatting found
        if len(before) == 0:
            return value
        # Return formatted value
        return before + value + Tput.sgr0()

    def get_value(self, *args, **kwargs):
        key = args[0]
        if (
            isinstance(key, str)
            and len(key) > 2
            and key[0] == key[-1]
            and key[0] in ("'", '"')
        ):
            # allow {"Hello"} type variables
            return key[1:-1]
        return super().get_value(*args, **kwargs)
