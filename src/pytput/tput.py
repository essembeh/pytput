from dataclasses import dataclass, field
from os import getenv
from subprocess import DEVNULL, PIPE, run


def check_env():
    return getenv("PYTPUT_DISABLE", "").strip().lower() in ("false", "", "0")


@dataclass
class TputWrapper:

    check_tty: bool = field(default=True)
    enabled: bool = field(init=False, default_factory=check_env)
    _cache: dict = field(init=False, default_factory=dict)

    def __exec(self, *args):
        try:
            if self.enabled:
                args = [str(x) for x in args]
                cmdid = " ".join(args)
                if cmdid not in self._cache:
                    self._cache[cmdid] = run(
                        ["tput"] + args, stdout=PIPE, stderr=DEVNULL, check=True
                    ).stdout.decode()
                return self._cache.get(cmdid, "")
        except BaseException:
            # In case of error, disable tput for next calls
            self.enabled = False
        return ""

    def colors(self):
        """
        Supported colors count
        """
        return int(self.__exec("colors") or "0")

    def colums(self):
        """
        Number of columns
        """
        return int(self.__exec("cols") or "0")

    def lines(self):
        """
        Number of lines
        """
        return int(self.__exec("lines") or "0")

    def sc(self):
        """
        Save the cursor position
        """
        return self.__exec("sc")

    def rc(self):
        """
        Restore the cursor position
        """
        return self.__exec("rc")

    def home(self):
        """
        Move the cursor to upper left corner (0,0)
        """
        return self.__exec("home")

    def cup(self, row, col):
        """
        Move the cursor to position row, col
        """
        return self.__exec("cup", row, col)

    def cud1(self):
        """
        Move the cursor down 1 line
        """
        return self.__exec("cud1")

    def cuu1(self):
        """
        Move the cursor up 1 line
        """
        return self.__exec("cuu1")

    def civis(self):
        """
        Set to cursor to be invisible
        """
        return self.__exec("civis")

    def cnorm(self):
        """
        Set the cursor to its normal state
        """
        return self.__exec("cnorm")

    def dim(self):
        """
        Start dim text
        """
        return self.__exec("dim")

    def bold(self):
        """
        Start bold text
        """
        return self.__exec("bold")

    def smul(self):
        """
        Start underlined text
        """
        return self.__exec("smul")

    def rmul(self):
        """
        End underlined text
        """
        return self.__exec("rmul")

    def rev(self):
        """
        Start reverse video
        """
        return self.__exec("rev")

    def blink(self):
        """
        Start blinking text
        """
        return self.__exec("blink")

    def invis(self):
        """
        Start invisible text
        """
        return self.__exec("invis")

    def smso(self):
        """
        Start "standout" mode
        """
        return self.__exec("smso")

    def rmso(self):
        """
        End "standout" mode
        """
        return self.__exec("rmso")

    def sgr0(self):
        """
        Turn off all attributes
        """
        return self.__exec("sgr0")

    def setaf(self, color: int):
        """
        Set foreground color
        """
        return self.__exec("setaf", color)

    def setab(self, color: int):
        """
        Set background color
        """
        return self.__exec("setab", color)

    def smcup(self):
        """
        Save screen contents
        """
        return self.__exec("smcup")

    def rmcup(self):
        """
        Restore screen contents
        """
        return self.__exec("rmcup")

    def el(self):
        """
        Clear from the cursor to the end of the line
        """
        return self.__exec("el")

    def el1(self):
        """
        Clear from the cursor to the beginning of the line
        """
        return self.__exec("el1")

    def ed(self):
        """
        Clear from the cursor to the end of the screen
        """
        return self.__exec("ed")

    def clear(self):
        """
        Clear the entire screen and home the cursor
        """
        return self.__exec("clear")


Tput = TputWrapper()
