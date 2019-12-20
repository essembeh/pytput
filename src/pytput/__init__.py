from pkg_resources import get_distribution

from pytput.formatter import TputFormatter, TputString, strcolor
from pytput.style import Style

__title__ = "pytput"
__version__ = get_distribution(__title__).version
__author__ = "Sébastien MB"
__license__ = "Mozilla Public License Version 2.0"
__license_url__ = "https://www.mozilla.org/en-US/MPL/2.0/"

__all__ = ["strcolor", "Style", "TputFormatter", "TputString"]
