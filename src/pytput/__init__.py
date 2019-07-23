from pytput.formatter import TputFormatter
from pytput.style import Style, Color
from pytput.tput import Tput
from pytput.utils import print_color, print_red, tput_format, tput_print
from pkg_resources import get_distribution

__title__ = "pytput"
__version__ = get_distribution(__title__).version
__author__ = "Sébastien MB"
__license__ = "Mozilla Public License Version 2.0"
__license_url__ = "https://www.mozilla.org/en-US/MPL/2.0/"

__all__ = [
    "TputFormatter",
    "Tput",
    "Style",
    "Color",
    "print_color",
    "print_red",
    "tput_format",
    "tput_print",
]

