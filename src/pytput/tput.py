import os
import subprocess

__TPUT_CACHE = {}


def tput_exec(*args, default=""):
    try:
        if not os.getenv("PYTPUT_DISABLE"):
            args = [str(x) for x in args]
            cmdid = " ".join(args)
            if cmdid not in __TPUT_CACHE:
                __TPUT_CACHE[cmdid] = subprocess.check_output(
                    ["tput"] + args, stderr=subprocess.DEVNULL
                ).decode()
            return __TPUT_CACHE.get(cmdid) or default
    except (BaseException):
        # In case of error, disable tput for next calls
        os.environ["PYTPUT_DISABLE"] = "1"
    return default


class Tput:
    """
    Tput wrapper
    """

    @property
    def colors(self):
        """
        Supported colors count
        """
        return int(tput_exec("colors", "0"))

    @property
    def colums(self):
        """
        Number of columns
        """
        return int(tput_exec("cols", "0"))

    @property
    def lines(self):
        """
        Number of lines
        """
        return int(tput_exec("lines", "0"))

    @property
    def sc(self):
        """
        Save the cursor position
        """
        return tput_exec("sc")

    @property
    def rc(self):
        """
        Restore the cursor position
        """
        return tput_exec("rc")

    @property
    def home(self):
        """
        Move the cursor to upper left corner (0,0)
        """
        return tput_exec("home")

    def cup(self, row, col):
        """
        Move the cursor to position row, col
        """
        return tput_exec("cup", row, col)

    @property
    def cud1(self):
        """
        Move the cursor down 1 line
        """
        return tput_exec("cud1")

    @property
    def cuu1(self):
        """
        Move the cursor up 1 line
        """
        return tput_exec("cuu1")

    @property
    def civis(self):
        """
        Set to cursor to be invisible
        """
        return tput_exec("civis")

    @property
    def cnorm(self):
        """
        Set the cursor to its normal state
        """
        return tput_exec("cnorm")

    @property
    def dim(self):
        """
        Start dim text
        """
        return tput_exec("dim")

    @property
    def bold(self):
        """
        Start bold text
        """
        return tput_exec("bold")

    @property
    def smul(self):
        """
        Start underlined text
        """
        return tput_exec("smul")

    @property
    def rmul(self):
        """
        End underlined text
        """
        return tput_exec("rmul")

    @property
    def rev(self):
        """
        Start reverse video
        """
        return tput_exec("rev")

    @property
    def blink(self):
        """
        Start blinking text
        """
        return tput_exec("blink")

    @property
    def invis(self):
        """
        Start invisible text
        """
        return tput_exec("invis")

    @property
    def smso(self):
        """
        Start "standout" mode
        """
        return tput_exec("smso")

    @property
    def rmso(self):
        """
        End "standout" mode
        """
        return tput_exec("rmso")

    @property
    def sgr0(self):
        """
        Turn off all attributes
        """
        return tput_exec("sgr0")

    def setaf(self, color: int):
        """
        Set foreground color
        """
        return tput_exec("setaf", color)

    def setab(self, color: int):
        """
        Set background color
        """
        return tput_exec("setab", color)

    @property
    def smcup(self):
        """
        Save screen contents
        """
        return tput_exec("smcup")

    @property
    def rmcup(self):
        """
        Restore screen contents
        """
        return tput_exec("rmcup")

    @property
    def el(self):
        """
        Clear from the cursor to the end of the line
        """
        return tput_exec("el")

    @property
    def el1(self):
        """
        Clear from the cursor to the beginning of the line
        """
        return tput_exec("el1")

    @property
    def ed(self):
        """
        Clear from the cursor to the end of the screen
        """
        return tput_exec("ed")

    @property
    def clear(self):
        """
        Clear the entire screen and home the cursor
        """
        return tput_exec("clear")
